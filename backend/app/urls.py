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
from rest_framework import routers
from rest_api.views import ArticleList
from rest_api.views import CommunityMembersAPIView
from rest_api.views import UserList, UserDetail
from rest_api.views import CommunityDetail, CommunityList
from rest_framework.urlpatterns import format_suffix_patterns

# api一覧
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', UserList.as_view()),
    path('api/users/<int:pk>/', UserDetail.as_view()),
    path('api/communities/', CommunityList.as_view()),
    path('api/communities/<int:pk>/', CommunityDetail.as_view()),
    path('api/communities/<int:pk>/users/', CommunityMembersAPIView.as_view()),
    path('api/articles/', ArticleList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

