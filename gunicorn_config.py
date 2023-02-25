import multiprocessing

# The number of worker processes for handling requests.
workers = multiprocessing.cpu_count() * 2 + 1

# The IP address and port number for the gunicorn server to bind to.
bind = '0.0.0.0:8000'

# The location of the Django app's WSGI application object.
# Replace "myapp" with the name of your Django app.
app_module = 'config.wsgi'

# The maximum number of requests a worker can handle before being recycled.
max_requests = 1000

# The maximum number of seconds a worker can be idle before being recycled.
timeout = 30

# Set the log level to INFO or DEBUG.
loglevel = 'INFO'
