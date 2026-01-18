# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Clone the voice-gender-classifier repository
RUN git clone https://github.com/JaesungHuh/voice-gender-classifier.git

# Copy application file
COPY app/ ./app/
COPY requirements.txt ./

RUN mv /voice-gender-classifier /voice_gender_classifier

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r voice_gender_classifier/requirements.txt

# Set environment variables
ENV PYTHONPATH="${PYTHONPATH}:/app/voice_gender_classifier"

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app/api.py"]
