from ..models import Article, Community,User
from ..serializer import  ArticleSerializer, CommunitySerializer, CommunityUsersSerializer 
from ..serializer import  CommunityArticlesSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from backend.rest_api import serializer

class CommunityArticleDetailPrivateAPIView(APIView):
    def get_object(self, community_id, article_id, user_id ):
        try:
            _ = Article.objects.get(article_id=article_id)
            user = User.objects.get(pk=user_id)
            community = user.community_set.get(pk=community_id)
            return community
        except Community.DoesNotExist:
            return Http404
    
    def get(self, request, community_id, article_id, user_id, format=None):
        snipet = self.get_object(community_id, article_id, user_id)
        serializer = CommunityUsersSerializer(snipet)
        return Response(serializer.data)


class CommunityArticleDetailAPIView(APIView):
    def get_object(self, community_id, article_id):
        try:
            community = Community.objects.get(pk=community_id)
            article = community.article_set.get(pk=article_id)
            return article
        except Community.DoesNotExist:
            return Http404

    def get(self, request, community_id, article_id, format=None):
        snippet = self.get_object(community_id, article_id)
        serializer = ArticleSerializer(snippet)
        return Response(serializer.data)
    
    # 投稿にユーザを追加するメソッド
    def post(self, request, format=None):
        serializer = CommunityArticlesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# コミュニティの記事一覧
class CommunityArticlesAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny, ]

    def get(self, request, pk, *args, **kwargs):
        community = get_object_or_404(Community, pk=pk)
        serializer = CommunityArticlesSerializer(community)
        return Response(
            serializer.data,
        )

# コミュニティに参加しているメンバーを取得する
class CommunityMembersAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny, ]

    def get(self, request, pk, *args, **kwargs):
        communities = get_object_or_404(Community, pk=pk)
        serializer = CommunityUsersSerializer(communities)
        return Response(
            serializer.data,
        )


# コミュニティ参加API
class CommunityJoin(APIView):
    def get_object(self, pk):
        try:
            return Community.objects.get(pk=pk)
        except Community.DoesNotExist:
            raise Http404

    # コミュニティ参加
    def post(self, request, format=None):
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # コミュニティ退会    
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
# コミュニティ一覧
class CommunityList(APIView):
    def get(self,request, format=None):
        communities = Community.objects.all()
        selializer = CommunitySerializer(communities, many=True)
        return Response(selializer.data)
    
    def post(self, request, format=None):
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# コミュニティ詳細ページのview
class CommunityDetail(APIView):
    def get_object(self, pk):
        try:
            return Community.objects.get(pk=pk)
        except Community.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CommunitySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CommunitySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)