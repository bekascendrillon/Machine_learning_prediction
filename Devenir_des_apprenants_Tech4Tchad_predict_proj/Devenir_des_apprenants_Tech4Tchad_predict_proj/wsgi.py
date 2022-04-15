"""
WSGI config for Devenir_des_apprenants_Tech4Tchad_predict_proj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Devenir_des_apprenants_Tech4Tchad_predict_proj.settings')

application = get_wsgi_application()
