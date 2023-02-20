# Use the official Python image as the base image
FROM python:3.7

# Set the working directory
WORKDIR /breakfast

# Copy the Flask microservice code into the image
COPY . /breakfast

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for Flask
ENV FLASK_APP=breakfast.py

# Expose port 5000 for the Flask microservice
EXPOSE 5000

# Run the Flask microservice
CMD ["flask", "run", "--host=0.0.0.0"]
