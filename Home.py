import streamlit as st

st.set_page_config(
    page_title="Home"
)

st.write("# Welcome to the Home Page!")

st.sidebar.success("Select a feature above.")

st.markdown(
    """
    ### Face Recognition
    Begin by registering your face on the **Register** page. 
    Simply upload a clear and high-quality image featuring a single face, 
    along with the corresponding name. 
    Once your face is registered, head over to the **Recognition** page and 
    effortlessly upload another photo. 
    Our advanced system will quickly analyze the image, 
    accurately recognizing the face and returning the associated name. 
    Remember, for optimal results, ensure your photos are clear and feature only one face. 
"""
)