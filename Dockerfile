# Use a slim version of Python to keep the image small (approx 120MB vs 900MB)
FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable real-time logging to the console
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Create a non-root user for security (Crucial for enterprise roles)
RUN adduser --disabled-password appuser

# Install dependencies first to leverage Docker's layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Switch to the non-root user
USER appuser

# The command to run your Triage Engine
CMD ["python", "Main.py"]
