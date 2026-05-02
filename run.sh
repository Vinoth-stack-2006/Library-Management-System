#!/bin/bash
set -e

# Navigate to pr1 directory (relative to script location)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR/pr1"

# Print debug info
echo "Working directory: $(pwd)"
echo "Python version: $(python --version)"
echo "PYTHONPATH: $PYTHONPATH"
echo "DJANGO_SETTINGS_MODULE: $DJANGO_SETTINGS_MODULE"

# Verify key files exist
echo "Checking pr1 package..."
ls -la pr1/__init__.py pr1/settings.py pr1/wsgi.py

echo "Starting Gunicorn..."
exec gunicorn \
  --workers 1 \
  --worker-class sync \
  --bind 0.0.0.0:8000 \
  --timeout 120 \
  --access-logfile - \
  --error-logfile - \
  pr1.wsgi:application
