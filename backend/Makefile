### バックエンドのセットアップをしていない場合以下のコマンドを使用
## ここから
# バックエンドセットアップに必要
setup-pip:
	pip install pipenv && pipenv install

#仮想環境に入る
in-pip:
	pipenv shell

#仮想環境に出る
out-pip:
	exit
## ここまで


# モデルの内容をデータベースに反映
migrate:
	python manage.py migrate

# docker内で実行
migrate-docker:
	docker-compose exec backend python manage.py  migrate --noinput

# サーバの起動
run-server:
	python manage.py runserver

# データベースの確認
# 「\l」でdb確認
ls-docker-db:
	docker-compose exec postgres psql --username=pos_db_user --dbname=sokuseki_db