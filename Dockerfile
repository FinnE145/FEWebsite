# Use official Python slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /opt/FEWebsite

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY . .

# Expose the Flask port
EXPOSE 5000

# Run the app when container starts
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
