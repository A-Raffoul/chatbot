from PIL import Image
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load an image using Pillow
# image_path='samples/sample_image.png'
image_path='samples/flight-sc.png'
# image_path = 'samples/PMC1626454_002_00.png'
# image_path = 'samples/PMC3826085_003_00.png'
# image_path = 'samples/image_1.png'
image = Image.open(image_path)

# Use pytesseract to perform OCR on the image
text = pytesseract.image_to_data(image)
print(text)

# Print the extracted text
output_file = 'pytessaract_output.txt'
with open(output_file, 'w') as file:
    file.write(text)