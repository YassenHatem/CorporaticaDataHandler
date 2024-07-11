from ..repositories.text_repository import TextRepository
from ..models.text_model import TextRecord
from ..utils.text_processing import summarize_text, keyword_extraction, sentiment_analysis, tsne_visualization

class TextService:
    def __init__(self):
        self.repository = TextRepository()

    def summarize_text(self, text_content):
        summary = summarize_text(text_content)
        self.repository.insert_one(TextRecord(text=text_content, summary=summary))
        return {"summary": summary}

    def extract_keywords(self, text_content):
        keywords = keyword_extraction(text_content)
        self.repository.insert_one(TextRecord(text=text_content, keywords=keywords))
        return {"keywords": keywords}

    def analyze_sentiment(self, text_content):
        sentiment = sentiment_analysis(text_content)
        self.repository.insert_one(TextRecord(text=text_content, sentiment=sentiment))
        return {"sentiment": sentiment}

    def tsne_visualization(self, texts):
        texts = [doc.text for doc in self.repository.find_all()]
        tsne_result = tsne_visualization(texts)
        return {"tsne": tsne_result.tolist()}
