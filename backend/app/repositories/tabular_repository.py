from .. import mongo
from ..models.tabular_model import TabularRecord

class TabularRepository:
    """
    Repository class for handling database operations related to tabular data.
    """
    def insert_many(self, records):
        """
        Inserts multiple records into the tabular collection.

        :param records: List of TabularRecord instances to be inserted.
        """
        mongo.db.tabular.insert_many([record.dict(by_alias=True) for record in records])

    def find(self, query):
        """
        Finds records in the tabular collection matching the query.

        :param query: Dictionary representing the query conditions.
        :return: List of TabularRecord instances matching the query.
        """
        results = mongo.db.tabular.find(query)
        return [TabularRecord(**result) for result in results]

    def find_one(self, query):
        """
        Finds records in the tabular collection matching the query.

        :param query: Dictionary representing the query conditions.
        :return: TabularRecord instances matching the query.
        """
        return mongo.db.tabular.find_one(query)


    def find_all(self):
        """
        Retrieves all records from the tabular collection.

        :return: List of TabularRecord instances.
        """
        results = mongo.db.tabular.find()
        return [TabularRecord(**result) for result in results]

    def insert_one(self, record):
        """
        Inserts a single record into the tabular collection.

        :param record: TabularRecord instance to be inserted.
        """
        mongo.db.tabular.insert_one(record.dict(by_alias=True))

    def update_one(self, record):
        """
        Updates a single record in the tabular collection.

        :param record: TabularRecord dictionary with updated data.
        """
        mongo.db.tabular.update_one({'_id': record.get("id")}, {"$set": record}, upsert=False)

    def delete_one(self, record_id):
        """
        Deletes a single record from the tabular collection.

        :param record_id: TabularRecord instance id to be deleted.
        """
        mongo.db.tabular.delete_one({'_id': record_id})
