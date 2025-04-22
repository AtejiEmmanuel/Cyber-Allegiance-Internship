# Use a lightweight official Python image for testing
FROM python:3.11-slim

# Create app directory inside container
WORKDIR /app

# Create a simple Python script
RUN echo "print('Hello, Docker!')" > app.py

# Run the Python script when the container starts running
CMD ["python", "app.py"]
