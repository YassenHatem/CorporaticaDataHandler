from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

def process_image(image):
    """
    Processes an image from a file.

    :param image: File object containing the image.
    :return: Processed PIL Image object.
    """
    img = Image.open(image)
    return img

def color_histogram(img, filename):
    """
    Generates the color histogram for an image and saves it as an image.

    :param img: PIL Image object.
    :param filename: Name of the file to save the histogram image.
    :return: Path to the histogram image.
    """
    img_array = np.array(img)
    color = ('b', 'g', 'r')
    plt.figure()
    for i, col in enumerate(color):
        histr = cv2.calcHist([img_array], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    histogram_dir = os.path.join(os.path.dirname(__file__), '../histograms')
    os.makedirs(histogram_dir, exist_ok=True)
    histogram_path = os.path.join(histogram_dir, f'{filename}_histogram.png')
    plt.savefig(histogram_path)
    plt.close()
    return histogram_path


def segmentation_mask(img):
    """
    Generates a segmentation mask for an image.

    :param img: PIL Image object.
    :return: PIL Image object representing the segmentation mask.
    """
    img_array = np.array(img.convert('L'))  # Convert image to grayscale
    _, mask = cv2.threshold(img_array, 128, 255, cv2.THRESH_BINARY)
    mask = Image.fromarray(mask)
    return mask

def resize_image(img, width, height):
    """
    Resizes an image to the specified width and height.

    :param img: PIL Image object.
    :param width: New width of the image.
    :param height: New height of the image.
    :return: Resized PIL Image object.
    """
    return img.resize((width, height))

def crop_image(img, left, top, right, bottom):
    """
    Crops an image to the specified coordinates.

    :param img: PIL Image object.
    :param left: Left coordinate.
    :param top: Top coordinate.
    :param right: Right coordinate.
    :param bottom: Bottom coordinate.
    :return: Cropped PIL Image object.
    """
    return img.crop((left, top, right, bottom))

def convert_image_format(img, format):
    """
    Converts an image to the specified format.

    :param img: PIL Image object.
    :param format: New format of the image (e.g., 'JPEG', 'PNG').
    :return: Converted PIL Image object.
    """
    img = img.convert(format)
    return img
