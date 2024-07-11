from flask import Blueprint, request, jsonify
from ..services.text_service import TextService

text_controller = Blueprint('text_controller', __name__)
text_service = TextService()

@text_controller.route('/summarize', methods=['POST'])
def summarize():
    text_content = request.json.get('text')
    response = text_service.summarize_text(text_content)
    return jsonify(response)

@text_controller.route('/keywords', methods=['POST'])
def keywords():
    text_content = request.json.get('text')
    response = text_service.extract_keywords(text_content)
    return jsonify(response)

@text_controller.route('/sentiment', methods=['POST'])
def sentiment():
    text_content = request.json.get('text')
    response = text_service.analyze_sentiment(text_content)
    return jsonify(response)

@text_controller.route('/tsne', methods=['POST'])
def tsne():
    texts = request.json.get('texts')
    response = text_service.tsne_visualization(texts)
    return jsonify(response)
