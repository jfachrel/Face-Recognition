# Face Recognition

### Dependencies
- pandas==1.3.3
- numpy==1.23.5
- flask==2.3.2
- mtcnn==0.1.1
- keras_facenet==0.3.2
- tensorflow==2.*
- pillow

example dataset: [face_recognition_dataset](https://drive.google.com/drive/folders/1uqJ0OP0RtV9hAuqQ4FMzM3nJL7YRJDT_?usp=sharing)

Accuracy and F1 Score on a Dataset of 25 Asian Male Faces:

<img src="https://github.com/jfachrel/Face-Recognition/blob/main/assets/accuracy%20and%20f1%20score.png">

## How to run this app

run the API via docker:

```bash
docker run -it -p 5000:5000  jfachrel/face_recognition:latest
```

### Register

API format:

```bash
payload = {
    'image': image_base64,
    'name': name
    }
```

or you can create python file `register.py` and then run `python register.py`

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

### Recognition

API format:

```bash
payload = {'image': image_base64}
```

or you can create python file `recognition.py` and then run `python recognition.py`

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

## Face recognition with streamlit

<img src="https://github.com/jfachrel/Face-Recognition/blob/main/assets/streamlit.png">

clone this repo

```bash
git clone https://github.com/jfachrel/Face-Recognition.git
```

install streamlit: `pip install streamlit`

run the API via docker:

```bash
docker run -it -p 5000:5000  jfachrel/face_recognition:latest
```

open other terminal and run streamlit

```bash
streamlit run Home.py
```

Streamlit will launch directly in your web browser, providing you with the ability to effortlessly perform face recognition by simply uploading your image and name.
