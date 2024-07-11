from ..repositories.images_repository import ImagesRepository
from ..models.images_model import ImageRecord
from ..utils.image_processing import process_image, color_histogram, segmentation_mask
import os
from PIL import Image

class ImagesService:
    def __init__(self):
        self.repository = ImagesRepository()

    def upload_images(self, files):
        file_paths = []
        for file in files:
            img = process_image(file)
            file_path = os.path.join('uploaded_images', file.filename)
            img.save(file_path)
            file_paths.append(file_path)
            self.repository.insert_one(ImageRecord(filename=file.filename, path=file_path))
        return {"message": "Images uploaded and processed successfully"}

    def get_color_histogram(self, filename):
        image_doc = self.repository.find_one({'filename': filename})
        if not image_doc:
            return {"error": "Image not found"}
        img = Image.open(image_doc.path)
        histogram = color_histogram(img)
        return {"histogram": histogram.tolist()}

    def get_segmentation_mask(self, filename):
        image_doc = self.repository.find_one({'filename': filename})
        if not image_doc:
            return {"error": "Image not found"}
        img = Image.open(image_doc.path)
        mask = segmentation_mask(img)
        mask_path = os.path.join('segmentation_masks', f"{filename}_mask.png")
        mask.save(mask_path)
        return {"message": "Segmentation mask generated successfully", "mask_path": mask_path}
