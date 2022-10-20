import json
from rest_api.models import CommunityArticlesOnly
from rest_api.models import User,Community,Article
from rest_api.models import User, Community,CommunityMembers,Article
from rest_api.serializer  import UserSerializer, CommunitySerializer,CommunityMembersSerializer,ArticleSerializer,CommunityUsersSerializer,CommunityArticlesSerializer
  
def test_community_articles():
    user = User.objects.get(user_id=1)
    # user1= User(password="password", email="test@example.com", user_name="test_user_article_1", address="test address")
    user2 = User.objects.get(user_id=2)

    community1 = Community.objects.get(community_id=1)
    user_1_community_1 = CommunityMembers(id=20, user_id=user, community_id=community1)
    user_1_community_1_2 = CommunityMembers(id=20,user_id=user2, community_id=community1)
    user_1_community_1.save()
    user_1_community_1_2.save()
    u_c_serializer_1 = CommunityUsersSerializer(community1)
    print(json.dumps(u_c_serializer_1.data))
    user_1_community_1.delete()
    user_1_community_1_2.delete()
    

    # article1 = Article(uri="http://...",user=user, article_name="test_article", article_content="article content test", meeting_time="2022-10-10")
    article1 = Article.objects.get(article_id=1)
    # article2 = Article.objects.create(article_id=2)
    article1.save()
    # article2.save()
    print(article1)
    community_article = CommunityArticlesOnly(community_id=community1, article_id=article1)
    # community_article2 = CommunityArticlesOnly(community_id=community1, article_id=article2)
    community_article.save()
    # community_article2.save()
    c = CommunityArticlesSerializer(community1)
    print(json.dumps(c.data ))
