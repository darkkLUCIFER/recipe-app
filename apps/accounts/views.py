from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.settings import api_settings

from apps.accounts.serializers import CreateUserSerializer, AuthTokenSerializer


class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
