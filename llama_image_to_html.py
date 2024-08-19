import requests
import os
import base64


# Your Hugging Face API token
API_TOKEN = os.getenv('HF_ACCESS_TOKEN')

# Define the headers with your token
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

image_path = "samples/PMC1626454_002_00.png"

# Load the image and convert it to base64
with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

# Define the model and API URL
model = "google/vit-base-patch16-224"
api_url = f"https://api-inference.huggingface.co/models/{model}"


# Prepare the request data
data = {
    "inputs": encoded_image,
}

# Send the request
response = requests.post(api_url, headers=headers, json=data)

# Print the output
print(response.json())
