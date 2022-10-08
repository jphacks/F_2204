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

# サーバの起動
run-server:
	python manage.py runserver