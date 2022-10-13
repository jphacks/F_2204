# dockerのビルドと起動
dc/up-d:
	docker-compose up -d

dc/up-build:
	docker-compose up --build -d

# コンテナ、イメージもろもろ全削除
dc/all-remove:
	docker-compose down --rmi all --volumes --remove-orphans