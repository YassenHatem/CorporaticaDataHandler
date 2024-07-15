from ..repositories.text_repository import TextRepository
from ..utils.text_processing import generate_summary, extract_keywords, analyze_sentiment, tsne_visualization


class TextService:
    """
    Service class for managing text records and applying text processing.
    """

    def __init__(self):
        """
        Initialize the TextService with a TextRepository instance.
        """
        self.repository = TextRepository()

    def create_text(self, text_record):
        """
        Create a new text record and process the text.

        Args:
            text_record (dict): The text record to create.

        Returns:
            str: The ID of the created text record.
        """
        text_record['summary'] = generate_summary(text_record['text'])
        text_record['keywords'] = extract_keywords(text_record['text'])
        text_record['sentiment'] = analyze_sentiment(text_record['text'])
        return self.repository.create(text_record)

    def get_text(self, text_id):
        """
        Retrieve a text record by its ID.

        Args:
            text_id (str): The ID of the text record.

        Returns:
            dict: The retrieved text record.
        """
        return self.repository.read(text_id)

    def update_text(self, text_id, text_record):
        """
        Update an existing text record by its ID and process the text.

        Args:
            text_id (str): The ID of the text record to update.
            text_record (dict): The updated text record.

        Returns:
            dict: The updated text record.
        """
        text_record['summary'] = generate_summary(text_record['text'])
        text_record['keywords'] = extract_keywords(text_record['text'])
        text_record['sentiment'] = analyze_sentiment(text_record['text'])
        return self.repository.update(text_id, text_record)

    def delete_text(self, text_id):
        """
        Delete a text record by its ID.

        Args:
            text_id (str): The ID of the text record to delete.
        """
        self.repository.delete(text_id)

    def list_texts(self):
        """
        Retrieve all text records.

        Returns:
            list: A list of all text records.
        """
        records = self.repository.list_all()
        # Convert ObjectId to string
        for record in records:
            record['_id'] = str(record['_id'])
        return records

    def tsne_visualization(self):
        """
        Perform t-SNE visualization on all text records.

        Returns:
            list: A list of 2D coordinates corresponding to the t-SNE visualization.
        """
        texts = [record['text'] for record in self.repository.list_all()]
        return tsne_visualization(texts)
