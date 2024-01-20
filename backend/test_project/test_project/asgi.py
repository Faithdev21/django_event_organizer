import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings')
import django

django.setup()

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from chat.middleware import JWTAuthMiddlewareStack
from chat.routing import websocket_urlpatterns

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": JWTAuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)),
    }
)
