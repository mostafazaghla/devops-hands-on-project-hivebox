# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages (in this case, argparse is built-in, no extra installs)

# Command to run the app
CMD ["python", "app.py"]