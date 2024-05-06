"""
ASGI config for seeran_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from messages.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seeran_backend.settings')

wsgi_application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": wsgi_application,  # Regular Django ASGI application for HTTP
        "websocket": AuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)  # WebSocket routing
        ),
    }
)