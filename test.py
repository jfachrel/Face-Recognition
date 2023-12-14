import base64
import requests

with open("dataset/test/Andrew.jpg", "rb") as image_file:
    # Read the image file as bytes
    image_data = image_file.read()

# Convert the image data to base64-encoded string
image_base64 = base64.b64encode(image_data).decode('utf-8')

url = 'http://localhost:8000/register'

# Set the JSON payload
payload = {
    'image': image_base64,
    'name' : "andrew"
    }

# Set the headers with 'Content-Type' as 'application/json'
headers = {
    'Content-Type': 'application/json'
    }
    
res = requests.post(url, json=payload, headers=headers)
message = res.json()
print(message)