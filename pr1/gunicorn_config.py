import multiprocessing
import os

# Gunicorn config for Render deployment
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"
timeout = 120
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
