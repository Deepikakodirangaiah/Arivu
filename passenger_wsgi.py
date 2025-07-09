import os
import sys

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Arivu.settings')

# Import the Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()