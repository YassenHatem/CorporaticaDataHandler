from flask import Blueprint, request, jsonify
from ..services.tabular_service import TabularService

tabular_controller = Blueprint('tabular_controller', __name__)
tabular_service = TabularService()


@tabular_controller.route('/upload', methods=['POST'])
def upload_tabular():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})

    response = tabular_service.upload_tabular(file)
    return jsonify(response)


@tabular_controller.route('/query', methods=['POST'])
def query_tabular():
    query = request.json.get('query')
    response = tabular_service.query_tabular(query)
    return jsonify(response)


@tabular_controller.route('/statistics', methods=['GET'])
def statistics():
    response = tabular_service.compute_statistics()
    return jsonify(response)


@tabular_controller.route('/create', methods=['POST'])
def create_record():
    data = request.json
    response = tabular_service.create_record(data)
    return jsonify(response)


@tabular_controller.route('/read', methods=['GET'])
def read_records():
    response = tabular_service.read_records()
    return jsonify(response)


@tabular_controller.route('/update', methods=['PUT'])
def update_record():
    data = request.json
    response = tabular_service.update_record(data)
    return jsonify(response)


@tabular_controller.route('/delete', methods=['DELETE'])
def delete_record():
    data = request.json
    response = tabular_service.delete_record(data)
    return jsonify(response)
