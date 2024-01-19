import os
from datetime import datetime

import django
import jwt
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections

from users.models import User

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")
django.setup()
ALGORITHM = "HS256"


class TokenAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        close_old_connections()
        token_key = (
            dict(
                (
                    x.split("=")
                    for x in scope.get("query_string", b"").decode().split("&")
                )
            )
        ).get("token", None)

        scope["user"] = await get_user(token_key)
        return await super().__call__(scope, receive, send)


@database_sync_to_async
def get_user(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=ALGORITHM)
    except jwt.PyJWTError:
        return AnonymousUser()

    token_exp = datetime.fromtimestamp(payload["exp"])
    if token_exp < datetime.utcnow():
        return AnonymousUser()

    try:
        user = User.objects.get(id=payload["user_id"])
    except User.DoesNotExist:
        return AnonymousUser()
    return user


def JWTAuthMiddlewareStack(inner):
    """Custom middleware."""
    return TokenAuthMiddleware(inner)
