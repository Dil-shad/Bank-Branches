import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import User


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = []

        auth_header = request.META.get('HTTP_AUTHORIZATION')
        # print(auth_header)
        if auth_header and auth_header.startswith('Bearer'):
            token = auth_header[7:].strip()

        else:
            token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:

            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user = User.objects.filter(id=payload['id']).first()
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        return (user, token)
