import pytesseract
from PIL import Image

# Specify the path to your image file
image_path = './92.png'


# Open image using PIL
image = Image.open(image_path)

# Perform OCR using pytesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
with open('double_order.txt', 'w', encoding='utf-8') as file:

    file.write(text)
print(f'The Result is same as following:\n{text}')