from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import User, Article
from django.utils import timezone

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_id", "user_name", "address")
        db_table="sokuseki_db"



class ArticleSerializer(serializers.ModelSerializer):
    article_id = serializers.IntegerField(read_only=True)
    uri = serializers.URLField(required=False,max_length=300, allow_blank=True)
    article_name = serializers.CharField(required=False,max_length=255)
    article_content = serializers.CharField(required=False, allow_blank=True, max_length=255)
    meeting_time = serializers.DateTimeField(required=False,default=timezone.now())
    created_at = serializers.DateTimeField(required=False,default=timezone.now())
    
    def create(self,validated_data):
        return Article.objects.create(**validated_data)