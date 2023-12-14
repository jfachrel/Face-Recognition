# Use a base image with Python installed
FROM python:3.8.16

# Set the working directory in the container
WORKDIR /app

# # Install OpenGL dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Install libglib2.0-0 package
RUN apt-get update && apt-get install -y libglib2.0-0

# Copy the requirements.txt file
COPY requirements.txt .

# Install the required dependencies
RUN pip install -U pip
RUN pip install -r requirements.txt

# Copy python files
COPY face_recognition.py .
COPY main.py .

# Expose the ports for Flask and Streamlit
EXPOSE 8000:8000

# Set the entry point command
CMD ["python", "main.py"]

