from .. import mongo
from ..models.tabular_model import TabularRecord
from bson.objectid import ObjectId

class TabularRepository:
    def insert_many(self, records):
        mongo.db.tabular.insert_many([record.dict(by_alias=True) for record in records])

    def find(self, query):
        results = mongo.db.tabular.find(query)
        return [TabularRecord(**result) for result in results]

    def find_all(self):
        results = mongo.db.tabular.find()
        return [TabularRecord(**result) for result in results]

    def insert_one(self, record):
        mongo.db.tabular.insert_one(record.dict(by_alias=True))

    def update_one(self, record):
        mongo.db.tabular.update_one({'_id': ObjectId(record.id)}, {"$set": record.dict(by_alias=True)}, upsert=False)

    def delete_one(self, record):
        mongo.db.tabular.delete_one({'_id': ObjectId(record.id)})
