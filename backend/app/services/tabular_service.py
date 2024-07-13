from ..repositories.tabular_repository import TabularRepository
from ..models.tabular_model import TabularRecord
from ..utils.data_processing import process_tabular, compute_statistics
import pandas as pd
import logging

class TabularService:
    """
    Service class for handling business logic related to tabular data.
    """
    def __init__(self):
        self.repository = TabularRepository()

    def upload_tabular(self, file):
        """
        Processes and uploads tabular data from a file.

        :param file: File object containing tabular data.
        :return: Response message indicating the status of the upload.
        """
        df = process_tabular(file)
        records = [TabularRecord(**record) for record in df.to_dict(orient='records')]
        self.repository.insert_many(records)
        return {"message": "File processed and data stored successfully"}

    def query_tabular(self, query):
        """
        Queries tabular data based on specified conditions.

        :param query: Dictionary representing the query conditions.
        :return: List of tabular records matching the query.
        """
        results = self.repository.find(query)
        return [record.dict() for record in results]

    def compute_statistics(self):
        """
        Computes advanced statistics for the tabular data.

        :return: Dictionary containing computed statistics.
        """
        data = self.repository.find_all()
        df = pd.DataFrame([record.dict() for record in data])
        stats = compute_statistics(df)
        return stats

    def create_record(self, data):
        """
        Creates a new record in the tabular data.

        :param data: Dictionary containing the data for the new record.
        :return: Response message indicating the status of the operation.
        """
        record = TabularRecord(**data)
        self.repository.insert_one(record)
        return {"message": "Data added successfully"}

    def read_records(self):
        """
        Reads all records from the tabular data.

        :return: List of all tabular records.
        """
        results = self.repository.find_all()
        return [record.dict() for record in results]

    def update_record(self, data):
        """
        Updates an existing record in the tabular data.

        :param data: Dictionary containing the updated data for the record.
        :return: Response message indicating the status of the operation.
        """
        self.repository.update_one(data)
        return {"message": "Data updated successfully"}

    def delete_record(self, data):
        """
        Deletes a record from the tabular data.

        :param data: Dictionary containing the identifier of the record to be deleted.
        :return: Response message indicating the status of the operation.
        """
        record_id = data.get("_id")
        logging.info(data)
        self.repository.delete_one(record_id)
        return {"message": "Data deleted successfully"}
