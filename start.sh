#!/bin/bash
set -e

# Start script for Render deployment

# Get the script directory (repo root)
REPO_ROOT="$(pwd)"
echo "Repository root: $REPO_ROOT"

# Navigate to pr1 directory
cd "$REPO_ROOT/pr1"
echo "Working directory: $(pwd)"

# Verify Django is properly configured
echo "DJANGO_SETTINGS_MODULE: $DJANGO_SETTINGS_MODULE"
echo "PYTHONPATH: $PYTHONPATH"

# List key files to verify structure
echo "Checking project structure..."
ls -la pr1/settings.py
ls -la manage.py

# Start gunicorn
echo "Starting Gunicorn..."
exec gunicorn \
  --workers 4 \
  --worker-class sync \
  --bind 0.0.0.0:${PORT:-8000} \
  --timeout 120 \
  --log-level info \
  --access-logfile - \
  pr1.wsgi:application
