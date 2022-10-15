from rest_framework import viewsets
from .models import User, Community
from .serializer import UserSerializer, CommunitySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer