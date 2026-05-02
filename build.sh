#!/bin/bash
set -e

echo "Starting Render build process..."

# Navigate to pr1 directory
cd pr1

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Running Django migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed successfully!"
