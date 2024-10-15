import multiprocessing

bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 120 
max_requests = 1000 
max_requests_jitter = 50 
accesslog = '-'
errorlog = '-'
loglevel = 'info'
