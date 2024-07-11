from ..repositories.tabular_repository import TabularRepository
from ..models.tabular_model import TabularRecord
from ..utils.data_processing import process_tabular, compute_statistics
import pandas as pd

class TabularService:
    def __init__(self):
        self.repository = TabularRepository()

    def upload_tabular(self, file):
        df = process_tabular(file)
        records = [TabularRecord(**record) for record in df.to_dict(orient='records')]
        self.repository.insert_many(records)
        return {"message": "File processed and data stored successfully"}

    def query_tabular(self, query):
        results = self.repository.find(query)
        return [record.dict() for record in results]

    def compute_statistics(self):
        data = self.repository.find_all()
        df = pd.DataFrame([record.dict() for record in data])
        stats = compute_statistics(df)
        return stats

    def create_record(self, data):
        record = TabularRecord(**data)
        self.repository.insert_one(record)
        return {"message": "Data added successfully"}

    def read_records(self):
        results = self.repository.find_all()
        return [record.dict() for record in results]

    def update_record(self, data):
        record = TabularRecord(**data)
        self.repository.update_one(record)
        return {"message": "Data updated successfully"}

    def delete_record(self, data):
        record = TabularRecord(**data)
        self.repository.delete_one(record)
        return {"message": "Data deleted successfully"}
