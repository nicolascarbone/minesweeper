from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class TokenViewSet(ObtainAuthToken):
    """
    Returns a fresh token for user with passed id credentials.
    """
    def post(self, request, pk=None):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
        })


class UserViewSet(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        user = User.objects.create_user(
            username=request.data.get('username'),
            is_superuser=1)
        user.set_password(request.data.get('password'))
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)
