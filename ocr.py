# pip install pytesseract Pillow
# Or you can use apt install tesseract-ocr for linux.

from PIL import Image
import pytesseract

# Load the image from the file
image_path = 'your_image.png'  # Replace with your image file path
img = Image.open(image_path)

# Use pytesseract to perform OCR on the image
extracted_text = pytesseract.image_to_string(img)

# Print the extracted text
print(extracted_text)
