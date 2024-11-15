# wsgi.py
import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for 'django' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings') 

# Get the WSGI application callable
application = get_wsgi_application()
