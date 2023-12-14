import pandas as pd
from flask import Flask, request, jsonify
import face_recognition as fr
from waitress import serve

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register(dataset='registered_faces'):
    # get data
    data = request.get_json()
    name = data['name']

    image = fr.base64_to_image(data['image'])

    face, message = fr.crop_image(image)

    if face is not None:
        embedding = fr.embedding(face)
        name = name.lower()
        df = fr.load_csv(dataset)
        
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
    image = fr.base64_to_image(data['image'])

    # detect face
    face, message = fr.crop_image(image)
    
    if face is not None:
        embedding = fr.embedding(face)
        
        df = fr.load_csv(dataset)
        value = df.iloc[:,:-1].values
        name = df['name']

        distance, name = fr.compute_distance(value, name, embedding)

        if distance < threshold:
            message = name
        else:
            message = 'your face is not registered'
    
    return jsonify(message)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)