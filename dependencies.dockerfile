FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip3 install --upgrade pip setuptools wheel
COPY requirements.txt .
RUN pip3 install -r requirements.txt
