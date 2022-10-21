from ..models import Article, Community, User
from ..serializer import ArticleSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions, generics
from django.db import transaction
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class AuthRegister(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(APIView):
    def get(self,request, format=None):
        users = User.objects.all()
        selializer = UserSerializer(users, many=True)
        return Response(selializer.data)
    
    # def post(self, request, format=None):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserArticleList(APIView):
    def get_object(self, pk):
        try:
            user =  User.objects.get(pk=pk)
            articles = user.article_set.all()
            return articles
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ArticleSerializer(snippet,many=True)
        return Response(serializer.data)

class UserArticleDetail(APIView):
    def get_object(self, user_id, article_id):
        try:
            user = User.objects.get(pk=user_id)
            article = user.article_set.get(pk=article_id)
            return article
        except User.DoesNotExist:
            return Http404

    def get(self, request, user_id, article_id, format=None):
        snippet = self.get_object(user_id, article_id)
        serializer = ArticleSerializer(snippet)
        return Response(serializer.data)
    