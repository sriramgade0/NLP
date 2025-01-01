from paddleocr import PaddleOCR
import re
import matplotlib.pyplot as plt
from PIL import Image

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Load Image
image_path = 'potato_chips_2q.png'  # Update with your image path
image = Image.open(image_path)

# Show the image (optional)
plt.imshow(image)
plt.axis('off')
plt.show()

# Perform OCR
result = ocr.ocr(image_path)

# Extract text and process it
ocr_text = "\n".join([line[1][0] for line in result[0]])
print("Extracted OCR Text:")
print(ocr_text)

# Define regex patterns for metadata extraction
patterns = {
    "Name": r"(?i)(name|product):?\s*(.+)",
    "Weight or Volume": r"(?i)(weight|volume):?\s*(\d+[\w\s]+)",
    "Nutrition Information": r"(?i)(nutrition(?:al)? information):?\s*((?:.|\n)*?)(?:ingredients|$)",
    "Ingredients": r"(?i)(ingredients):?\s*((?:.|\n)*?)$"
}

# Extract and display metadata
metadata = {}
for key, pattern in patterns.items():
    match = re.search(pattern, ocr_text)
    if match:
        metadata[key] = match.group(2).strip()

# Display the extracted metadata
print("\nExtracted Metadata:")
for key, value in metadata.items():
    print(f"{key}: {value}")
