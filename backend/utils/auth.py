import jwt
from functools import wraps
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

def require_jwt(secret_name):
    """
    Decorator factory: checks “Authorization: Bearer <token>” against
    settings.SECRET_NAME and puts decoded payload into request.jwt.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(self, request, *args, **kwargs):
            auth = request.headers.get('Authorization', '')
            if not auth.startswith('Bearer '):
                return Response({"detail": "Missing or invalid auth header"},
                                status=status.HTTP_401_UNAUTHORIZED)
            token = auth.split()[1]
            secret = getattr(settings, secret_name, None)
            try:
                payload = jwt.decode(token, secret, algorithms=[settings.JWT_ALGORITHM])
            except jwt.PyJWTError:
                return Response({"detail": "Invalid or expired token"},
                                status=status.HTTP_401_UNAUTHORIZED)
            request.jwt = payload
            return view_func(self, request, *args, **kwargs)
        return _wrapped
    return decorator

# two decorators:
user_token_required = require_jwt('JWT_USER_SECRET')
service_token_required = require_jwt('JWT_SERVICE_SECRET')