# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (Render/Railway use dynamic PORT)
EXPOSE 8000

# Start command
CMD ["python", "main.py"]
