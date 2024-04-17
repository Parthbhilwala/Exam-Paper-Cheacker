import io
import os
from google.cloud import vision
from google.cloud.vision_v1 import Image

current_directory = os.path.dirname(os.path.abspath(__file__))
# Construct the complete file path for your Google Cloud service account key JSON file
file_name = os.path.join(current_directory, 'corded-pivot-403608-8bbffa01aba8.json')

# Set the path to your Google Cloud service account key JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = file_name

def extract_text_from_image(image_path):
    client = vision.ImageAnnotatorClient()

    with io.open(image_path, "rb") as image_file:
        content = image_file.read()

    image = Image(content=content)

    response = client.text_detection(image=image)

    texts = response.text_annotations

    if texts:
        print("Text extracted from the image:")
        extracted_text =texts[0].description

        lines = extracted_text.split('\n')

        # Concatenate the lines into a single line
        concatenated_text = ' '.join(lines)
        # extracted_text = ''.join([text.description[0] for text in texts[1:]])  # Extract the first character from each line
        print(concatenated_text.upper())
    else:
        print("No text found in the image.")

if __name__ == "__main__":
    image_path = "D:/SEM 5/python/python lab/proj/EPC/backend/images/student_mcq_cropped.jpg"
    extract_text_from_image(image_path)
