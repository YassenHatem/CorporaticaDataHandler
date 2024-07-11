from flask import Blueprint, request, jsonify
from ..services.images_service import ImagesService

images_controller = Blueprint('images_controller', __name__)
images_service = ImagesService()

@images_controller.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    files = request.files.getlist('file')

    response = images_service.upload_images(files)
    return jsonify(response)

@images_controller.route('/color_histogram', methods=['GET'])
def get_color_histogram():
    filename = request.args.get('filename')
    response = images_service.get_color_histogram(filename)
    return jsonify(response)

@images_controller.route('/segmentation_mask', methods=['GET'])
def get_segmentation_mask():
    filename = request.args.get('filename')
    response = images_service.get_segmentation_mask(filename)
    return jsonify(response)
