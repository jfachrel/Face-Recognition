import streamlit as st
import requests
import base64
import time

st.set_page_config(
    page_title="Recognition"
)

st.markdown("# Face Recognition")
st.sidebar.header("Recognition")

uploaded_file = st.file_uploader(label="Choose an image", type=['jpg', 'jpeg','png'])

url = 'http://api:8000/recognition'

if uploaded_file is not None:
    st.image(uploaded_file, use_column_width=True)
    image_data = uploaded_file.read()

    # Convert the image data to base64-encoded string
    image_base64 = base64.b64encode(image_data).decode('utf-8')

    # Set the JSON payload
    payload = {'image': image_base64}

    # Set the headers with 'Content-Type' as 'application/json'
    headers = {'Content-Type': 'application/json'}
    
if st.button('Submit'):
    with st.spinner("Loading... ⏳"):
        time.sleep(1)
        res = requests.post(url, json=payload, headers=headers)
        if res.status_code == 200:
            st.success("Name: " + res.json().capitalize())
        else:
            st.error("Error sending image to the API.")
            st.write("Status Code:", res.status_code)
            st.write("Error Message:", res.text)
    