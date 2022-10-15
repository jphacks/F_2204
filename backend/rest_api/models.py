from tabnanny import verbose
from unicodedata import category, name
from django.db import models
from django.utils import timezone
# ユーザ情報
class User(models.Model):
    user_id =  models.AutoField(verbose_name="ユーザID",primary_key=True)
    user_name = models.CharField(verbose_name="ユーザ名",max_length=255)
    address = models.CharField(verbose_name="住所",max_length=255)
    created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True) 


# Community Table
class Community(models.Model):
    community_id = models.AutoField(verbose_name="Community ID",primary_key=True)
    community_name = models.CharField(verbose_name="Community Name",max_length=255)

# connect users and community table
class User_Community(models.Model):
    member_id = models.AutoField(verbose_name="Member ID",primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)

class Article(models.Model):
    article_id = models.AutoField(verbose_name="ID",primary_key=True)
    uri = models.URLField(verbose_name="URI", max_length=300, null=True)
    article_name = models.CharField(verbose_name="投稿タイトル",max_length=255)
    article_content = models.TextField(verbose_name="投稿内容",max_length=255)
    meeting_time = models.DateTimeField(verbose_name="開催日時", default=timezone.now())
    created_at = models.DateTimeField(verbose_name="投稿作成日時", default=timezone.now())

class Article_Community(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE)