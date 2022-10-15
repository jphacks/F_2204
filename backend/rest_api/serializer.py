from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import User, Community, User_Community, Article, Article_Community


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_id", "user_name", "address")
        
class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ("community_id", "community_name")
        
class User_CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Community
        fields = ('member_id', 'user', 'community')
        
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('article_id', 'uri', 'article_name', 'article_content', 'meeting_time')
        
class Article_CommunitySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Article_Community
        fields = ('article_id', 'community_id')