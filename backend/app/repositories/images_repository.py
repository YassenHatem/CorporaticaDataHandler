from .. import mongo
from ..models.images_model import ImageRecord

class ImagesRepository:
    """
    Repository class for handling database operations related to images.
    """
    def insert_many(self, records):
        """
        Inserts multiple records into the images collection.

        :param records: List of ImageRecord instances to be inserted.
        """
        mongo.db.images.insert_many([record.dict(by_alias=True) for record in records])

    def find(self, query):
        """
        Finds records in the images collection matching the query.

        :param query: Dictionary representing the query conditions.
        :return: List of ImageRecord instances matching the query.
        """
        results = mongo.db.images.find(query)
        return [ImageRecord(**result) for result in results]

    def find_one(self, query):
        """
        Finds records in the tabular collection matching the query.

        :param query: Dictionary representing the query conditions.
        :return: TabularRecord instances matching the query.
        """
        return mongo.db.images.find_one(query)


    def find_all(self):
        """
        Retrieves all records from the images collection.

        :return: List of ImageRecord instances.
        """
        results = mongo.db.images.find()
        return [ImageRecord(**result) for result in results]

    def insert_one(self, record):
        """
        Inserts a single record into the images collection.

        :param record: ImageRecord instance to be inserted.
        """
        mongo.db.images.insert_one(record.dict(by_alias=True))

    def update_one(self, record):
        """
        Updates a single record in the images collection.

        :param record: ImageRecord dictionary with updated data.
        """
        mongo.db.images.update_one({'_id': record.get("id")}, {"$set": record}, upsert=False)

    def delete_one(self, record_id):
        """
        Deletes a single record from the images collection.

        :param record_id: ImageRecord instance id to be deleted.
        """
        mongo.db.images.delete_one({'_id': record_id})
