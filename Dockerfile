# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Set environment variables (use defaults or placeholders)

ENV SQLALCHEMY_DATABASE_URI=${DATABASE_URL}

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]