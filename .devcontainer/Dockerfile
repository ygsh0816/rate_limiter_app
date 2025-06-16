# Use the official Python Dev Container image as the base
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Install Redis CLI (optional, for debugging Redis)
RUN apt-get update && apt-get install -y redis-tools && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /workspace

# Copy the project files into the container
COPY . /workspace
