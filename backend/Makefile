### バックエンドのセットアップをしていない場合以下のコマンドを使用
## ここから
# バックエンドセットアップに必要

install:
	pip install -r requirements.txt

# 仮想環境起動ずみ、docker起動ずみ
user-test-list-one:
	http http://localhost:8000/api/users/ 
	http http://localhost:8000/api/users/1/

# docker内で実行
migrate:
	docker-compose exec backend python manage.py  migrate --noinput

migration:
	docker-compose exec backend python manage.py   makemigrations
# サーバの起動
run:
	docker-compose exec backend python manage.py runserver

shell:
	docker-compose exec backend python manage.py shell
create-superuser:
	docker-compose exec backend python manage.py createsuperuser
# データベースの確認
# 「\l」でdb確認
ls-docker-db:
	docker-compose exec db psql --username=pos_db_user --dbname=sokuseki_db

shell-create-user:
	make shell

	from rest_api.models import User
	from rest_api.serializer  import UserSerializer
	from rest_framework.renderers import JSONRenderer
	from rest_framework.parsers import JSONParser
	user = User(password="password", email="test@example.com", user_name="test_user", address="test address")
	user.save()
	userserializer2 = UserSerializer(user2)
	userserializer2.data
	user2 = User(password="password2", email="test2@example.com", user_name="test_user_2", address="test address")
	user2.save()
	userserializer2 = UserSerializer(user2)
	userserializer2.data