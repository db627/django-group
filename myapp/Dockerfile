# Use a stable Python version as the base image
FROM python:3.12.0a1-buster
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
COPY * /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the Django project into the container
COPY . /app/


# Expose the port the application will run on
EXPOSE 8000
# Command to run the application

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
