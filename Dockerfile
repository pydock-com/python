# Dockerfile for running an external Python repository as a service on port 8080

# Use an official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Install Git (if not already installed)
RUN apt-get update && apt-get install -y git
