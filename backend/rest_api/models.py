from unicodedata import category, name
from django.db import models

# ユーザ情報
class User(models.Model):
    user_id =  models.AutoField(verbose_name="ユーザID",primary_key=True)
    user_name = models.CharField(verbose_name="ユーザ名",max_length=255)
    address = models.CharField(verbose_name="住所",max_length=255)
    created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True) 