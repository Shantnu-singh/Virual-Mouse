# Use a base image with Python 
FROM python:3.10-slim

# Install minimal OpenGL dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory =
WORKDIR /app

# Copy the application 
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose Port
EXPOSE 8000

# Run Command
CMD ["python", "virtual_mouse.py"]