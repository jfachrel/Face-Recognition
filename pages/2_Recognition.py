import streamlit as st
import requests
import base64

st.set_page_config(
    page_title="Recognition"
)

st.markdown("# Face Recognition")
st.sidebar.header("Recognition")

uploaded_file = st.file_uploader(label="Choose an image", type=['jpg', 'jpeg','png'])

url = 'http://localhost:5000//recognition'

if uploaded_file is not None:
    image_data = uploaded_file.read()

    # Convert the image data to base64-encoded string
    image_base64 = base64.b64encode(image_data).decode('utf-8')

    # Set the JSON payload
    payload = {'image': image_base64,
               'name':'name'}

    # Set the headers with 'Content-Type' as 'application/json'
    headers = {'Content-Type': 'application/json'}
    
    res = requests.post(url, json=payload, headers=headers)
    message = res.json()

    st.write(message)
    