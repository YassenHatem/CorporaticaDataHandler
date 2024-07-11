# backend/app/utils/text_processing.py
from textblob import TextBlob
from sklearn.manifold import TSNE
import numpy as np

def summarize_text(text):
    blob = TextBlob(text)
    summary = blob.sentences[:5]  # Simple summarization
    return ' '.join([str(sentence) for sentence in summary])

def keyword_extraction(text):
    blob = TextBlob(text)
    keywords = blob.noun_phrases
    return keywords

def sentiment_analysis(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment

def tsne_visualization(texts):
    tsne = TSNE(n_components=2)
    vectors = [TextBlob(text).words for text in texts]
    tsne_result = tsne.fit_transform(np.array(vectors))
    return tsne_result
