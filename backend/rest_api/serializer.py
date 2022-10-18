from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import CommunityMembers, User, Article, Community
from django.utils import timezone

DB_NAME="sokuseki_db"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        db_table=DB_NAME


class CommunityMembersSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        # user_idが一致する行を取得
        user_obj = UserSerializer(instance=obj.user_id)
        return user_obj.data
    
    
    class Meta:
        model = CommunityMembers
        fields='__all__'


class CommunityUsersSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()

    def get_users(self, obj):
        communities = Community.objects.get(pk=obj.pk)
        serializers = CommunityMembersSerializer(
            communities.users_communities.all(), 
            many=True
        )
        return serializers.data


    class Meta:
        model = Community
        fields="__all__"



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