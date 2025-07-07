# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir pyrogram flask tgcrypto

# Expose port 8000 for health checks
EXPOSE 8000

# Run the bot
CMD ["python", "main.py"]