import pytesseract
import cv2
import numpy as np
from PIL import Image


# If tesseract is NOT in PATH, uncomment and adjust:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(file_path):

    # Load image
    image = cv2.imread(file_path)

    if image is None:
        raise Exception("Invalid image file")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Noise removal
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Thresholding
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Convert to PIL for pytesseract
    pil_img = Image.fromarray(thresh)

    # Extract text
    text = pytesseract.image_to_string(pil_img)

    return text