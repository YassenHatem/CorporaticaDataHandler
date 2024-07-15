from .. import mongo
from bson.objectid import ObjectId


class TextRepository:
    """
    Repository class for handling text records in MongoDB.
    """

    def create(self, text_record):
        """
        Insert a new text record into the database.

        Args:
            text_record (dict): The text record to insert.

        Returns:
            str: The ID of the inserted text record.
        """
        result = mongo.db.texts.insert_one(text_record)
        return str(result.inserted_id)

    def read(self, text_id):
        """
        Retrieve a text record by its ID.

        Args:
            text_id (str): The ID of the text record.

        Returns:
            dict: The retrieved text record.
        """
        return mongo.db.texts.find_one({"_id": ObjectId(text_id)})

    def update(self, text_id, text_record):
        """
        Update an existing text record by its ID.

        Args:
            text_id (str): The ID of the text record to update.
            text_record (dict): The updated text record.

        Returns:
            dict: The updated text record.
        """
        text_record.pop('_id')
        mongo.db.texts.update_one({"_id": ObjectId(text_id)}, {"$set": text_record})

    def delete(self, text_id):
        """
        Delete a text record by its ID.

        Args:
            text_id (str): The ID of the text record to delete.
        """
        mongo.db.texts.delete_one({"_id": ObjectId(text_id)})

    def list_all(self):
        """
        Retrieve all text records.

        Returns:
            list: A list of all text records.
        """
        return list(mongo.db.texts.find())
