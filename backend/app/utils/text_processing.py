from nltk.sentiment.vader import SentimentIntensityAnalyzer
from rake_nltk import Rake
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.manifold import TSNE


def generate_summary(text):
    """
    Generate a summary for the given text.

    Args:
        text (str): The text to summarize.

    Returns:
        str: The generated summary.
    """
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 2)  # Summarize to 2 sentences
    return " ".join(str(sentence) for sentence in summary)


def extract_keywords(text):
    """
    Extract keywords from the given text.

    Args:
        text (str): The text to extract keywords from.

    Returns:
        list: A list of extracted keywords.
    """
    rake = Rake()
    rake.extract_keywords_from_text(text)
    return rake.get_ranked_phrases()


def analyze_sentiment(text):
    """
    Perform sentiment analysis on the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        float: The sentiment polarity of the text.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment['compound']


def tsne_visualization(texts):
    """
    Perform t-SNE visualization on a list of texts.

    Args:
        texts (list): A list of text strings.

    Returns:
        list: A list of 2D coordinates corresponding to the t-SNE visualization.
    """
    # Convert texts to TF-IDF vectors
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    # Set perplexity based on the number of samples
    perplexity = min(30, X.shape[0] - 1)

    tsne = TSNE(n_components=2, perplexity=perplexity, random_state=0)
    tsne_results = tsne.fit_transform(X.toarray())
    return tsne_results.tolist()
