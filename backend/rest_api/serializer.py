from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
<<<<<<< HEAD
from .models import User, Community, User_Community, Article, Article_Community
=======
from .models import CommunityMembers, User, Article, Community
from django.utils import timezone
>>>>>>> master

DB_NAME="sokuseki_db"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
<<<<<<< HEAD
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
=======
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

    class Meta:
        model = Article
        db_table=DB_NAME
        fields = "__all__"
    

class CommunitySerializer(serializers.ModelSerializer):
    community_id = serializers.IntegerField(read_only=True)
    community_name = serializers.CharField(required=False,max_length=255)

    class Meta:
        model = Community
        db_table=DB_NAME
        fields = ("community_id", "community_name")
>>>>>>> master
