import pandas as pd
import numpy as np
import os
import base64
from io import BytesIO
from PIL import Image
from mtcnn.mtcnn import MTCNN
from keras_facenet import FaceNet

def crop_image(image_buffer, threshold=0.95):
    image = Image.open(image_buffer)
    image = np.asarray(image)

    # detect face
    detector = MTCNN()
    results = [detection for detection in detector.detect_faces(image) if detection['confidence'] > threshold]

    message = ''
    face = None
    if len(results) == 0:
        message = 'No face detected'
    if len(results) > 1:
        message = 'More than one face is detected'
    if len(results) == 1:
        # crop image
        x1, y1, w, h = results[0]['box']
        x2, y2 = x1 + w, y1 + h
        
        face = image[y1:y2, x1:x2]

        # resize image
        face = Image.fromarray(face)
        face = face.resize((160,160))
        face = np.asarray(face)
        # transform face into one sample
        face = np.expand_dims(face, axis=0)

    return face, message

def embedding(image):
    embedding = FaceNet().embeddings(image)
    return embedding

def load_csv(dataset="registered_faces"):
    if os.path.exists(f'{dataset}.csv') == False: 
        # create empty table with 512 columns + name column
        columns = [i for i in range(512)]
        columns.append('name')
        df = pd.DataFrame(columns=columns)

        df.to_csv(f'{dataset}.csv',index=False)
    else:
        df = pd.read_csv(f'{dataset}.csv')
    
    return df

def base64_to_image(image_base64):
    image_data = base64.b64decode(image_base64)
    image = BytesIO(image_data)
    return image

def compute_distance(value, name, embedding):
    values = []
    names = []
    for i,j in zip(value,name):
        distance = FaceNet().compute_distance(i,embedding[0]) # cosine similarity
        values.append(distance)
        names.append(j)

    df_distance = pd.DataFrame({'distance':values, 'name':names})
    distance = df_distance.sort_values('distance')['distance'].iloc[0] # sort values by dinstace
    name = df_distance.sort_values('distance')['name'].iloc[0]

    return distance, name