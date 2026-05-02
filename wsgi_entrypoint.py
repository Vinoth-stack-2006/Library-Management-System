#!/usr/bin/env python
"""
WSGI entrypoint for Render deployment.
This script ensures the pr1 directory is in the Python path before starting Gunicorn.
"""

import os
import sys
import subprocess
from pathlib import Path

# Get the directory where this script is located (repo root)
REPO_ROOT = Path(__file__).parent.resolve()
PR1_DIR = REPO_ROOT / 'pr1'

print(f"Repository root: {REPO_ROOT}")
print(f"PR1 directory: {PR1_DIR}")

# Add pr1 to Python path
sys.path.insert(0, str(PR1_DIR))
os.chdir(str(PR1_DIR))

print(f"Changed working directory to: {os.getcwd()}")
print(f"Python path: {sys.path[:3]}")

# Set environment variables if not already set
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pr1.settings')
os.environ.setdefault('PYTHONPATH', str(PR1_DIR))

print(f"DJANGO_SETTINGS_MODULE: {os.environ['DJANGO_SETTINGS_MODULE']}")
print(f"PYTHONPATH: {os.environ['PYTHONPATH']}")

# Import and start Gunicorn
from gunicorn.app.wsgiapp import run

if __name__ == '__main__':
    sys.argv = ['gunicorn', 'pr1.wsgi:application']
    run()
