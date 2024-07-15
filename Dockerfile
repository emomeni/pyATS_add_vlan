# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory
WORKDIR /fuzz

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Run the fuzzing tests
ENTRYPOINT ["python", "pyats_addvlan_ossfuzz.py"]
