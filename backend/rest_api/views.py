from rest_framework import viewsets
from .models import User, Community, User_Community, Article
from .serializer import UserSerializer, CommunitySerializer, User_CommunitySerializer,ArticleSerializer, Article_CommunitySerialzer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    
class User_CommunityViewSet(viewsets.ModelViewSet):
    queryset = User_Community.objects.all()
    serializer_class = User_CommunitySerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class Article_CommunityViewSet(viewsets.ModelViewSet):
    queryset = Article_Community.objects.all()
    serializer_class = Article_CommunitySerialzer