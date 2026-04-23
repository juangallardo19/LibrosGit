import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'proyecto'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
