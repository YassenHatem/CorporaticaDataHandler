from flask import Blueprint, request, jsonify
from ..services.images_service import ImagesService

images_controller = Blueprint('images_controller', __name__)
images_service = ImagesService()


@images_controller.route('/upload', methods=['POST'])
def upload_images():
    """
    Endpoint for uploading images.

    :return: JSON response with the status of the upload.
    """
    files = request.files.getlist('images')
    if not files:
        return jsonify({"error": "No images provided"})

    response = images_service.upload_images(files)
    return jsonify(response)


@images_controller.route('/histogram/<filename>', methods=['GET'])
def get_color_histogram(filename):
    """
    Endpoint for generating and retrieving the color histogram of an image.

    :return: Response containing the histogram image file.
    """
    return images_service.get_color_histogram(filename)


@images_controller.route('/segmentation/<filename>', methods=['GET'])
def get_segmentation_mask(filename):
    """
    Endpoint for generating and retrieving the segmentation mask of an image.

    :return: JSON response with the segmentation mask path.
    """
    return images_service.get_segmentation_mask(filename)


@images_controller.route('/resize', methods=['POST'])
def resize_image():
    """
    Endpoint for resizing an image.

    :return: JSON response with the resized image path.
    """
    data = request.json
    filename = data['filename']
    width = data['width']
    height = data['height']

    response = images_service.resize_image(filename, width, height)
    return jsonify(response)


@images_controller.route('/crop', methods=['POST'])
def crop_image():
    """
    Endpoint for cropping an image.

    :return: JSON response with the cropped image path.
    """
    data = request.json
    filename = data['filename']
    left = data['left']
    top = data['top']
    right = data['right']
    bottom = data['bottom']

    response = images_service.crop_image(filename, left, top, right, bottom)
    return jsonify(response)


@images_controller.route('/convert', methods=['POST'])
def convert_image_format():
    """
    Endpoint for converting the format of an image.

    :return: JSON response with the converted image path.
    """
    data = request.json
    filename = data['filename']
    format = data['format']

    response = images_service.convert_image_format(filename, format)
    return jsonify(response)
