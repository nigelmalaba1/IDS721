# Use the official Python image as the base image
FROM python:3.7

# Set the working directory
WORKDIR /breakfastapp

# Copy the Flask microservice code into the image
COPY . /breakfastapp

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for Flask
ENV FLASK_APP=breakfastapp.py

# Expose port 5000 for the Flask microservice
EXPOSE 5000

# Run the Flask microservice
CMD ["flask", "run", "--host=0.0.0.0"]
