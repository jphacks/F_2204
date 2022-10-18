### バックエンドのセットアップをしていない場合以下のコマンドを使用
## ここから
# バックエンドセットアップに必要

install:
	pip install -r requirements.txt


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


# 条件：仮想環境起動ずみ、docker起動ずみ
check-user:
	docker-compose exec backend http http://localhost:8000/api/users/ 
	docker-compose exec backend http http://localhost:8000/api/users/1/

check-community:
	docker-compose exec backend http http://localhost:8000/api/communities/
	docker-compose exec backend http http://localhost:8000/api/communities/1/

check-articles:
	docker-compose exec backend http  http://localhost:8000/api/articles/