# Use an official Python runtime as the base image
FROM python:3.10-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Make port 80 available to the world outside this container
EXPOSE 80

# Define the command to run your application
CMD ["gunicorn", "-c", "gunicorn_config.py", "subOverTime:app"]
