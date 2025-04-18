# Set the Python version as a build-time argument with Python 3.12 as the default
ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH"  

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libpq-dev \
        libjpeg-dev \
        libcairo2 \
        gcc \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Create and activate virtual environment inside the container
RUN python -m venv $VIRTUAL_ENV

# Upgrade pip
RUN pip install --upgrade pip

# Set working directory
WORKDIR /code

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Define entrypoint script
ENTRYPOINT ["./entrypoint.sh"]

# Default command to run the application
CMD ["gunicorn", "FIRST.wsgi:application", "--bind", "0.0.0.0:8000"]
