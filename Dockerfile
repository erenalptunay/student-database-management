# Use Python 3.12.4 slim image
FROM python:3.12.4-slim

# Create a working directory
WORKDIR /app

# Copy the requirements file and the rest of the project files into the container
COPY requirements.txt requirements.txt
COPY . .

# Install the required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Start the application
CMD ["sh", "-c", "python setup.py && python main.py"]
