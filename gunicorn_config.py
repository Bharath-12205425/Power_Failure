import os

bind = f"0.0.0.0:{os.environ.get('PORT', '10000')}"
backlog = 2048

workers = 1
worker_class = 'sync'
worker_connections = 1000
timeout = 120
keepalive = 5

max_requests = 1000
max_requests_jitter = 100

accesslog = '-'
errorlog = '-'
loglevel = 'info'

proc_name = 'power_prediction_app'

daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

preload_app = True

def on_starting(server):
    server.log.info("Starting Power Prediction App with memory-optimized settings")
    server.log.info(f"Workers: {workers}, Timeout: {timeout}s")

def worker_int(worker):
    worker.log.info("Worker received INT or QUIT signal")

def worker_abort(worker):
    worker.log.info("Worker received SIGABRT signal")
