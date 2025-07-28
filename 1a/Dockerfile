# Use official lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your script and any other files (e.g. input.pdf)
COPY . .

# Command to run the script
CMD ["python", "extractor.py"]
