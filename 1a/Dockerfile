FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libglib2.0-0 libgl1-mesa-glx libxrender1 libsm6 libxext6 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
COPY 1a.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "1a.py"]
