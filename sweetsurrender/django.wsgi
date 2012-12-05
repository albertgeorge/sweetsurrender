import os
import sys

path = '/usr/local/lib/python2.7/site-packages/sweetsurrender'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'sweetsurrender.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()