"""
WSGI config for IS_CHAT project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from chats.consumers import PracticeConsumer
from django.urls import path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IS_CHAT.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": URLRouter([
     path('ws/practice', PracticeConsumer.as_asgi())
])
})
