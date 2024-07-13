from ..repositories.images_repository import ImagesRepository
from ..models.images_model import ImageRecord
from ..utils.image_processing import process_image, color_histogram, segmentation_mask, resize_image, crop_image, convert_image_format
import os
from PIL import Image
from flask import send_from_directory, current_app

class ImagesService:
    """
    Service class for handling business logic related to images.
    """
    def __init__(self):
        self.repository = ImagesRepository()
        self.uploaded_images_dir = 'uploaded_images'
        self.resized_images_dir = 'resized_images'
        self.cropped_images_dir = 'cropped_images'
        self.converted_images_dir = 'converted_images'
        self.segmentation_masks_dir = 'segmentation_masks'
        self.histograms_dir = 'histograms'

    def _ensure_directories_exist(self):
        """
        Ensures that necessary directories for storing images exist.
        """
        os.makedirs(os.path.join(current_app.root_path, self.uploaded_images_dir), exist_ok=True)
        os.makedirs(os.path.join(current_app.root_path, self.resized_images_dir), exist_ok=True)
        os.makedirs(os.path.join(current_app.root_path, self.cropped_images_dir), exist_ok=True)
        os.makedirs(os.path.join(current_app.root_path, self.converted_images_dir), exist_ok=True)
        os.makedirs(os.path.join(current_app.root_path, self.segmentation_masks_dir), exist_ok=True)
        os.makedirs(os.path.join(current_app.root_path, self.histograms_dir), exist_ok=True)

    def upload_images(self, files):
        """
        Processes and uploads images from files.

        :param files: List of file objects containing images.
        :return: Response message indicating the status of the upload.
        """
        self._ensure_directories_exist()
        file_paths = []
        for file in files:
            img = process_image(file)
            file_path = os.path.join(current_app.root_path, self.uploaded_images_dir, file.filename)
            img.save(file_path)
            file_paths.append(file_path)
            self.repository.insert_one(ImageRecord(filename=file.filename, path=file_path))
        return {"message": "Images uploaded and processed successfully"}

    def get_color_histogram(self, filename):
        """
        Generates and retrieves the color histogram for an image.

        :param filename: Name of the image file.
        :return: Response containing the histogram image file.
        """
        self._ensure_directories_exist()
        image_doc = self.repository.find_one({'filename': filename})
        if not image_doc:
            return {"error": "Image not found"}
        img = Image.open(image_doc.get("path"))
        histogram_path = color_histogram(img, filename)
        return send_from_directory(os.path.join(current_app.root_path, self.histograms_dir), os.path.basename(histogram_path))

    def get_segmentation_mask(self, filename):
        """
        Generates and retrieves the segmentation mask for an image.

        :param filename: Name of the image file.
        :return: Dictionary containing the segmentation mask path.
        """
        self._ensure_directories_exist()
        image_doc = self.repository.find_one({'filename': filename})
        if not image_doc:
            return {"error": "Image not found"}
        img = Image.open(image_doc.get("path"))
        mask = segmentation_mask(img)
        mask_path = os.path.join(current_app.root_path, self.segmentation_masks_dir, f"{filename}_mask.png")
        mask.save(mask_path)
        return send_from_directory(os.path.join(current_app.root_path, self.segmentation_masks_dir),
                                   os.path.basename(mask_path))


    def resize_image(self, filename, width, height):
        """
        Resizes an image to the specified width and height.

        :param filename: Name of the image file.
        :param width: New width of the image.
        :param height: New height of the image.
        :return: Dictionary containing the resized image path.
        """
        self._ensure_directories_exist()
        image_doc = self.repository.find_one({'filename': filename})
        if not image_doc:
            return {"error": "Image not found"}
        img = Image.open(image_doc.get("path"))
        resized_img = resize_image(img, width, height)
        resized_path = os.path.join(current_app.root_path, self.resized_images_dir, f"{filename}_resized.png")
        resized_img.save(resized_path)
        return {"message": "Image resized successfully", "resized_path": resized_path}

    def crop_image(self, filename, left, top, right, bottom):
        """
        Crops an image to the specified coordinates.

        :param filename: Name of the image file.
        :param left: Left coordinate.
        :param top: Top coordinate.
        :param right: Right coordinate.
        :param bottom: Bottom coordinate.
        :return: Dictionary containing the cropped image path.
        """
        self._ensure_directories_exist()
        image_doc = self.repository.find_one({'filename': filename})
        if not image_doc:
            return {"error": "Image not found"}
        img = Image.open(image_doc.get("path"))
        cropped_img = crop_image(img, left, top, right, bottom)
        cropped_path = os.path.join(current_app.root_path, self.cropped_images_dir, f"{filename}_cropped.png")
        cropped_img.save(cropped_path)
        return {"message": "Image cropped successfully", "cropped_path": cropped_path}

    def convert_image_format(self, filename, format):
        """
        Converts an image to the specified format.

        :param filename: Name of the image file.
        :param format: New format of the image (e.g., 'JPEG', 'PNG').
        :return: Dictionary containing the converted image path.
        """
        self._ensure_directories_exist()
        image_doc = self.repository.find_one({'filename': filename})
        if not image_doc:
            return {"error": "Image not found"}
        img = Image.open(image_doc.get("path"))
        converted_img = convert_image_format(img, format)
        converted_path = os.path.join(current_app.root_path, self.converted_images_dir, f"{filename}.{format.lower()}")
        converted_img.save(converted_path, format=format)
        return {"message": "Image format converted successfully", "converted_path": converted_path}
