from .. import mongo
from ..models.images_model import ImageRecord

class ImagesRepository:
    def insert_one(self, record):
        mongo.db.images.insert_one(record.dict(by_alias=True))

    def find_one(self, query):
        result = mongo.db.images.find_one(query)
        if result:
            return ImageRecord(**result)
        return None
