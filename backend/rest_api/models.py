from unicodedata import category, name
from django.db import models

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
class Member(models.Model):
    member_id = models.AutoField(verbose_name="Member ID",primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)