from PIL import Image
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print(pytesseract.get_tesseract_version())



# Load an image using Pillow
image = Image.open('samples/sample_image.png')

# Use pytesseract to perform OCR on the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
