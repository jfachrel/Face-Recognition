import pandas as pd
import numpy as np
import os
import base64
from io import BytesIO
from PIL import Image
from mtcnn.mtcnn import MTCNN
from keras_facenet import FaceNet
from flask import Flask, request, jsonify

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

def load_csv(dataset):
    if os.path.exists(f'{dataset}.csv') == False: 
        # create empty table with 512 columns + name column
        columns = [i for i in range(512)]
        columns.append('name')
        df = pd.DataFrame(columns=columns)

        df.to_csv(f'{dataset}.csv',index=False)
    else:
        df = pd.read_csv(f'{dataset}.csv')
    
    return df

app = Flask('face_recognition')

@app.route('/register', methods=['POST'])
def register(dataset='registered_faces'):
    # get data
    data = request.get_json()
    name = data['name']

    image_base64 = data['image']
    # Decode the base64-encoded image
    image_data = base64.b64decode(image_base64)
    # Create a BytesIO object to work with the image data
    image_buffer = BytesIO(image_data)

    face, message = crop_image(image_buffer)

    if face is not None:
        embedding = FaceNet().embeddings(face)
        name = name.lower()
        df = load_csv(dataset)
        
        # add new embedding
        new_embedding = pd.DataFrame([embedding[0]], columns=df.columns[:-1])
        new_df= pd.concat([df.iloc[:,:-1], new_embedding], ignore_index=True)

        # add new name 
        name_list = []
        for i in df['name']:
            name_list.append(i)
        name_list.append(name)
        new_df['name']=name_list

        new_df.to_csv(f'{dataset}.csv',index=False) # save to csv
        message = 'face registered successfully'
    
    return jsonify(message)


@app.route('/recognition', methods=['POST'])
def recognition(dataset='registered_faces', threshold=0.3):
    # get data
    data = request.get_json()
    image_base64 = data['image']
    
    # Decode the base64-encoded image
    image_data = base64.b64decode(image_base64)
    # Create a BytesIO object to work with the image data
    image_buffer = BytesIO(image_data)

    # detect face
    face, message = crop_image(image_buffer)
    
    if face is not None:
        embedding = FaceNet().embeddings(face)
        
        df = load_csv(dataset)
        x = df.iloc[:,:-1].values
        y = df['name']
        x_list = []
        y_list = []
        for i,j in zip(x,y):
            distance = FaceNet().compute_distance(i,embedding[0]) # cosine similarity
            x_list.append(distance)
            y_list.append(j)

        df_distance = pd.DataFrame({'distance':x_list, 'name':y_list})
        distance = df_distance.sort_values('distance')['distance'].iloc[0] # sort values by dinstace

        if distance < threshold:
            message = df_distance.sort_values('distance')['name'].iloc[0] # get the name
        else:
            message = 'your face is not registered'
    
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)