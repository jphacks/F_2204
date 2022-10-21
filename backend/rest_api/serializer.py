from rest_framework import serializers
from .models import CommunityArticlesOnly
from .models import CommunityMembers, User, Article, Community
from django.utils import timezone 
from rest_framework import permissions
DB_NAME="sokuseki_db"

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile', 'password')

    def create(self, validated_data):
        return User.objects.create_user(request_data=validated_data)

class UserSerializer(serializers.ModelSerializer):
    permission_classes = [permissions.IsAuthenticated]
    password = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = User
        fields = '__all__'
        db_table=DB_NAME


class CommunityArticle(serializers.ModelSerializer):
    article = serializers.SerializerMethodField()

    def get_article(self, obj):
        article_obj = ArticleSerializer(instance=obj.article_id)
        return article_obj.data
    
    class Meta:
        model = CommunityArticlesOnly
        fields="__all__"


# コミュニティのユーザを取得
class CommunityMembersSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        # user_idが一致する行を取得
        user_obj = UserSerializer(instance=obj.user_id)
        return user_obj.data
    
    
    class Meta:
        model = CommunityMembers
        fields='__all__'



class CommunityArticlesSerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()

    def get_articles(self, obj):
        community = Community.objects.get(pk=obj.pk)
        serializer = CommunityArticle(
            community.articles_communities.all(),
            many=True
        )
        return serializer.data
    
    class Meta:
        model = Community
        fields="__all__"


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
