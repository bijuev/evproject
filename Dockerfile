# Use the official Python image as a base image with Python 3.10
FROM python:3.10-slim

# Set environment variables to avoid Python writing .pyc files and buffer issues
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev

# Copy the requirements file to the working directory
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project to the working directory
COPY . /app/

# Expose the port the Django app will run on
EXPOSE 8000

# Run Gunicorn using the config file
CMD ["gunicorn", "--config", "/app/gunicorn.conf.py", "--bind", "0.0.0.0:8000", "mysite.wsgi:application"]
