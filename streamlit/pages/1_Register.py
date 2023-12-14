import streamlit as st
import requests
import base64
import time

st.set_page_config(
    page_title="Register"
)

st.markdown("# Face Registration")
st.sidebar.header("Register")

uploaded_file = st.file_uploader(label="Choose an image", type=['jpg', 'jpeg','png'])
name = st.text_input('Name:')

url = 'http://api:8000/register'

if uploaded_file is not None:
    st.image(uploaded_file, caption=name, use_column_width=True)

    # Convert the image data to base64-encoded string
    image_data = uploaded_file.read()
    image_base64 = base64.b64encode(image_data).decode('utf-8')
    
    if name != "":
        # Set the JSON payload
        payload = {
            'image': image_base64,
            'name': name
        }

        # Set the headers with 'Content-Type' as 'application/json'
        headers = {
            'Content-Type': 'application/json'
        }
    else:
        st.error("Name can not empty")

if st.button("Register"):
    with st.spinner("Registering face... ⏳"):
        time.sleep(1)
        res = requests.post(url, json=payload, headers=headers)
        # Check the response
        if res.status_code == 200:
            st.success(res.json().capitalize())
        else:
            st.error("Error sending image to the API.")
            st.write("Status Code:", res.status_code)
            st.write("Error Message:", res.text)