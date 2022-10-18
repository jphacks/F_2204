from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import User, Article, Community
from django.utils import timezone

DB_NAME="sokuseki_db"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_id", "user_name", "address")
        db_table=DB_NAME



class ArticleSerializer(serializers.ModelSerializer):
    article_id = serializers.IntegerField(read_only=True)
    uri = serializers.URLField(required=False,max_length=300, allow_blank=True)
    article_name = serializers.CharField(required=False,max_length=255)
    article_content = serializers.CharField(required=False, allow_blank=True, max_length=255)
    meeting_time = serializers.DateTimeField(required=False,default=timezone.now())
    created_at = serializers.DateTimeField(required=False,default=timezone.now())
    
    def create(self,validated_data):
        return Article.objects.create(**validated_data)


class CommunitySerializer(serializers.ModelSerializer):
    community_id = serializers.IntegerField(read_only=True)
    community_name = serializers.CharField(required=False,max_length=255)

    class Meta:
        model = Community
        db_table=DB_NAME
        fields = ("community_id", "community_name")