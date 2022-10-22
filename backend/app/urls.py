"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_api.views.community import CommunityArticleDetailAPIView
from rest_api.views.community import CommunityArticlesAPIView
from rest_api.views import UserArticleList, UserArticleDetail, UserList, UserDetail
from rest_api.views import ArticleList
from rest_api.views import CommunityDetail, CommunityList, CommunityMembersAPIView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# api一覧
urlpatterns = [
    path('api/articles/', ArticleList.as_view()),
    path('api/', include('rest_api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),


    path('api/users/', UserList.as_view()),
    path('api/users/<int:pk>/', UserDetail.as_view()),
    path('api/users/<int:pk>/articles/', UserArticleList.as_view()),
    path('api/users/<int:user_id>/articles/<int:article_id>/',
         UserArticleDetail.as_view()),
    path('api/communities/', CommunityList.as_view()),
    path('api/communities/<int:pk>/', CommunityDetail.as_view()),
    path('api/communities/<int:pk>/users/', CommunityMembersAPIView.as_view()),
    path('api/communities/<int:pk>/articles/',
         CommunityArticlesAPIView.as_view()),  # コミュニティの記事一覧取得API
    path('api/communities/<int:community_id>/articles/<int:article_id>/',
         CommunityArticleDetailAPIView.as_view()),  # コミュニティの記事一覧取得API
]

urlpatterns = format_suffix_patterns(urlpatterns)
