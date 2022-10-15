from rest_framework import viewsets
from .models import User, Community, User_Community
from .serializer import UserSerializer, CommunitySerializer, User_CommunitySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    
class User_CommunityViewSet(viewsets.ModelViewSet):
    queryset = User_Community.objects.all()
    serailizer_class = User_CommunitySerializer
    
