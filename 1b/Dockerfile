# Use official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies for PyMuPDF
RUN apt-get update && apt-get install -y \
    libglib2.0-0 libgl1-mesa-glx libxrender1 libsm6 libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Install PyMuPDF directly since we don't have requirements.txt
RUN pip install pymupdf

# Copy your script into the image
COPY 1b.py .

# Set default command to run your script
CMD ["python", "1b.py"]
