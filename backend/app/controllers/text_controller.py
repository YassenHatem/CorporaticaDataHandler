from flask import Blueprint, request, jsonify
from ..services.text_service import TextService

text_controller = Blueprint('text_controller', __name__)
text_service = TextService()


@text_controller.route('/create', methods=['POST'])
def create_text():
    """
    Create a new text record.

    Returns:
        Response: JSON response containing the ID of the created text record.
    """
    text_record = request.json
    text_id = text_service.create_text(text_record)
    return jsonify({"id": text_id})


@text_controller.route('/read/<text_id>', methods=['GET'])
def read_text(text_id):
    """
    Retrieve a text record by its ID.

    Args:
        text_id (str): The ID of the text record.

    Returns:
        Response: JSON response containing the text record.
    """
    text_record = text_service.get_text(text_id)
    return jsonify(text_record)


@text_controller.route('/update/<text_id>', methods=['PUT'])
def update_text(text_id):
    """
    Update an existing text record by its ID.

    Args:
        text_id (str): The ID of the text record.

    Returns:
        Response: JSON response containing the updated text record.
    """
    text_record = request.json
    updated_record = text_service.update_text(text_id, text_record)
    return jsonify(updated_record)


@text_controller.route('/delete/<text_id>', methods=['DELETE'])
def delete_text(text_id):
    """
    Delete a text record by its ID.

    Args:
        text_id (str): The ID of the text record.

    Returns:
        Response: JSON response confirming the deletion.
    """
    text_service.delete_text(text_id)
    return jsonify({"message": "Text deleted successfully"})


@text_controller.route('/list', methods=['GET'])
def list_texts():
    """
    Retrieve all text records.

    Returns:
        Response: JSON response containing a list of all text records.
    """
    texts = text_service.list_texts()
    return jsonify(texts)


@text_controller.route('/tsne', methods=['GET'])
def tsne_visualization():
    """
    Perform t-SNE visualization on all text records.

    Returns:
        Response: JSON response containing the t-SNE visualization coordinates.
    """
    tsne_results = text_service.tsne_visualization()
    return jsonify(tsne_results)
