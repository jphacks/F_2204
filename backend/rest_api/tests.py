#テストに必要なライブラリ
from logging import raiseExceptions
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import *
from django.utils import timezone
from django.test import Client

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

#多対多のUnit Testをどう描くか
class CommunityTest(TestCase):
    def test_save_and_recieve_community(self):
        user1 = User.objects.create(
          user_id = '01',
          password="01",
          email="01@gmail.com",
          user_name="Kan",
          address="Hukuoka",
        )
        
        user2 = User.objects.create(
          user_id = '02',
          password="02",
          email="02@gmail.com",
          user_name="Ken",
          address="Kumamoto",
        )
        
        user3 = User.objects.create(
          user_id = '03',
          password="03",
          email="03@gmail.com",
          user_name="Rin",
          address="Hokkaid",
        )
        
        user4 = User.objects.create(
          user_id = '04',
          password="04",
          email="04@gmail.com",
          user_name="shin",
          address="Okinawa",
        )
        
        community1 = Community.objects.create(
          community_id = '1',
          community_name = 'test1',
        )
        
        community2 = Community.objects.create(
          community_id = '2',
          community_name = 'test2',
        )
        
        user1.save()
        user2.save()
        user3.save()
        community1.save()
        community2.save()
        
        #community追加
        community1.users.add(user1)
        community1.users.add(user2)
        community2.users.add(user1)
        community2.users.add(user3)
        community = Community.objects.all()
        TestCase().assertEqual(community1.community_id, 1)
        TestCase().assertEqual(community2.community_name, 'test2')
        result1 = community1.users.all()
        list_users = [entry for entry in result1]  # converts ValuesQuerySet into Python list
        if user1 not in list_users:
          raise ValueError("this user is not in community")
        elif user4 not in list_users:
          print('OK')
        
        result2 = community2.users.all()
        list_users = [entry for entry in result2]
        if user1 not in list_users:
          raise ValueError("this user is not in community")
        elif user4 not in list_users:
          print('OK')
        # print(type([repr(user1)]))
        # print(type(list(community1.users.all())[0]))
        # TestCase().assertEqual(list(community1.users.all())[0], type(repr(user1))
        
          #最終的に削除する
        user1.delete()
        user2.delete()
        user3.delete()
        community1.delete()
        community2.delete()
               

class ArticleTest(TestCase):
    def test_save_and_recieve_article(self):
        user1 = User.objects.create(
          user_id = '01',
          password="01",
          email="01@gmail.com",
          user_name="Kan",
          address="Hukuoka",
        )
        article1 = Article.objects.create(
          user = user1,
          uri = 'https://aaaaaa',
          article_name = 'event1',
          article_content='イベント1',
        )
        
        article2 = Article(
          user = user1,
          uri = 'https://aaaaaa',
          article_name = 'event2',
          article_content='イベント2',
        )
        
        just_before_article = Article.objects.all()[0]
        TestCase().assertEqual(just_before_article.article_id, 2)
        TestCase().assertEqual(just_before_article.user.user_name, 'Kan')
        TestCase().assertEqual(just_before_article.article_name, 'event1')
        TestCase().assertEqual(just_before_article.article_content, 'イベント1')
        
    
class ArticleCommunityTest(TestCase):
    def test_save_and_recieve_articleCommunity(self):
        user1 = User.objects.create(
          user_id = '01',
          password="01",
          email="01@gmail.com",
          user_name="Kan",
          address="Hukuoka",
        )
        article1 = Article.objects.create(
          user = user1,
          uri = 'https://aaaaaa',
          article_name = 'event1',
          article_content='イベント1',
        )
        community1 = Community.objects.create(
          community_id = '1',
          community_name = 'test1',
        )
        
        article_community = Article_Community.objects.create(
          article_id = article1,
          community_id = community1
        )
        
        saved_article_community = Article_Community.objects.all()[0]
        
        TestCase().assertEqual(saved_article_community.article_id.article_id, 1)
        TestCase().assertEqual(saved_article_community.community_id.community_id, 1)
        # TestCase().assertEqual(saved_article_community.community_id, 1)
        
        