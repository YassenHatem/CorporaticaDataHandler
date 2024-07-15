import random
from faker import Faker
from pymongo import MongoClient
from app.utils.text_processing import generate_summary, extract_keywords, analyze_sentiment
from app.models.tabular_model import TabularRecord


fake = Faker()

# MongoDB Configuration
client = MongoClient("mongodb://localhost:27017/")
db = client.dataHandler

# Collection References
tabular_collection = db.tabular
text_collection = db.texts

def seed_tabular_data(n=1000):
    """
    Seed the tabular collection with n records.

    Args:
        n (int): Number of records to seed.
    """
    tabular_data = []
    for _ in range(n):
        record = {
            "name": fake.word(),
            "value": random.randint(1, 100)
        }
        tabular_data.append(TabularRecord(**record))

    tabular_collection.insert_many([record.dict(by_alias=True) for record in tabular_data])
    print(f"Seeded {n} records into tabular collection.")

def seed_text_data(n=1000):
    """
    Seed the text collection with n records.

    Args:
        n (int): Number of records to seed.
    """
    text_data = []
    for _ in range(n):
        text = fake.paragraph(nb_sentences=10)
        record = {
            "text": text,
            "summary": generate_summary(text),
            "keywords": extract_keywords(text),
            "sentiment": analyze_sentiment(text),
        }
        text_data.append(record)

    text_collection.insert_many(text_data)
    print(f"Seeded {n} records into text collection.")

if __name__ == "__main__":
    # Seed Data
    seed_tabular_data(1000)
    seed_text_data(1000)
