#テストに必要なライブラリ
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import *
from django.utils import timezone

class UserTest(TestCase):
    # def test_is_empty(self):
    #   """初期状態では何も登録されていないことをチェック"""  
    #   saved_posts = User.objects.all()
    #   self.assertEqual(saved_posts.count(), 0)
    
    def test_save_and_recieve_user(self):
        user = User.objects.create(
            user_id=00, 
            password='test00', 
            email='00@gmail.com',
            user_name='taro',
            address='Onohara',
        )
        user.save()
        saved_users = User.objects.all()
        just_before_user = saved_users[0]
        TestCase().assertEqual(just_before_user.user_id, 00)
        TestCase().assertEqual(just_before_user.password, 'test00',msg='Equal')
        TestCase().assertEqual(just_before_user.email, '00@gmail.com',msg='Equal')
        TestCase().assertEqual(just_before_user.user_name, 'taro', msg='Equal')
        TestCase().assertEqual(just_before_user.address, 'Onohara', msg='Equal')
        

        
        
    
