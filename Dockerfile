# Use an official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-alpine

# Python won’t try to write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /mymind

# Add system dependencies
RUN apk update && \
    apk add --no-cache git gcc musl-dev postgresql-dev bash graphviz graphviz-dev


# Install Python dependencies
COPY requirements.txt /mymind
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt --no-cache-dir

# Copy the content of the local src directory to the working directory
COPY . /mymind

# Specify the command to run on container start
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mymind.wsgi:application"]
