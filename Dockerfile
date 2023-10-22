FROM python:3.11

WORKDIR /opt/qa_app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
