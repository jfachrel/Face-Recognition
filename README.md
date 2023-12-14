# Face Recognition

<img src="https://github.com/jfachrel/Face-Recognition/blob/main/assets/streamlit.png">

### Requirements
1. Docker
2. Docker Compose

example dataset: [face_recognition_dataset](https://drive.google.com/drive/folders/1uqJ0OP0RtV9hAuqQ4FMzM3nJL7YRJDT_?usp=sharing)

Accuracy and F1 Score on a Dataset of 25 Asian Male Faces:

<img src="https://github.com/jfachrel/Face-Recognition/blob/main/assets/accuracy%20and%20f1%20score.png">

## How To Run This App

clone this repo:
```bash
git clone https://github.com/jfachrel/Face-Recognition.git
```

- Via docker-compose:
```bash
docker-compose up
```

or

- Open the `run.sh` file

## API Format

- **Register:**

```bash
payload = {
    'image': image_base64,
    'name': name
    }
```

or you can create a python file `register.py` and then run `python register.py`

```bash
import requests
import base64

url = 'http://localhost:5000/register'

# Open the image file
image_path = 'image.jpg' # input image path
name = 'name' # input name

with open(image_path, 'rb') as image_file:
    # Read the image data
    image_data = image_file.read()

# Convert the image data to base64-encoded string
image_base64 = base64.b64encode(image_data).decode('utf-8')

# Set the JSON payload
payload = {
    'image': image_base64,
    'name': name
    }

# Set the headers with 'Content-Type' as 'application/json'
headers = {'Content-Type': 'application/json'}

res = requests.post(url = url ,json=payload, headers=headers)
print(res.json()) 
 ```

- **Recognition:**

```bash
payload = {'image': image_base64}
```

or you can create a python file `recognition.py` and then run `python recognition.py`

```bash
import requests
import base64

url = 'http://localhost:5000/recognition'

# Open the image file
image_path = 'image.jpg' # input image path

with open(image_path, 'rb') as image_file:
    # Read the image data
    image_data = image_file.read()

# Convert the image data to base64-encoded string
image_base64 = base64.b64encode(image_data).decode('utf-8')

# Set the JSON payload
payload = {'image': image_base64}

# Set the headers with 'Content-Type' as 'application/json'
headers = {'Content-Type': 'application/json'}

res = requests.post(url = url ,json=payload, headers=headers)
print(res.json())
 ```
