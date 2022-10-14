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

create-superuser:
	docker-compose exec backend python manage.py createsuperuser
# データベースの確認
# 「\l」でdb確認
ls-docker-db:
	docker-compose exec db psql --username=pos_db_user --dbname=sokuseki_db