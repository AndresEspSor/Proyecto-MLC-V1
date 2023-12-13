FROM python:3.11-slim

# Set the working directory to /code
WORKDIR /code

# Copy the entire application directory into the container at /app
COPY . /code

# Install the dependencies
RUN python -m pip install --no-cache-dir --user -r requirements.txt

# Expose the desired port
EXPOSE 80

ENV FLASK_APP=app.py

# Set the entrypoint to run the Flask application
# ENTRYPOINT gunicorn -w 4 -b 0.0.0.0:5000 app:app
CMD ["python", "-m", "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

# Set the author label
LABEL author="PePr Digital"