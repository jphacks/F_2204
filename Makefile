# dockerのビルドと起動
dc/up-build:
	docker-compose up --build

# コンテナ、イメージもろもろ全削除
dc/all-remove:
	docker-compose down --rmi all --volumes --remove-orphans