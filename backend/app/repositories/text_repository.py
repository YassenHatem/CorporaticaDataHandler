from .. import mongo
from ..models.text_model import TextRecord

class TextRepository:
    def insert_one(self, record):
        mongo.db.texts.insert_one(record.dict(by_alias=True))

    def find_all(self):
        results = mongo.db.texts.find()
        return [TextRecord(**result) for result in results]
