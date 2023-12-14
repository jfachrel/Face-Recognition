# Use a base image with Python installed
FROM python:3.8

EXPOSE 8501

WORKDIR /app

COPY . .

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["streamlit", "run", "Home.py"]

