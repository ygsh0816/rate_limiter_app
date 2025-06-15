FROM python:3.10

# Install Redis CLI
RUN apt-get update && apt-get install -y redis-tools

# Set the working directory
WORKDIR /workspace

# Copy the project files
COPY . /workspace

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt