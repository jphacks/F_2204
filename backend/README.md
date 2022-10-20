# テストについて
DRF(Django REST Framework)におけるUnit Testについて記載する。
## 確認方法
1. docker 起動 ```make dc/up-buid```
2. ```docker exec -it f_2204-backend-1 /bin/sh``` でコンテナ内に入る
3. コンテナ内で ```python manage.py makemigration```
4. ```python manage.py migrate``` にてマイグレーションを行う。
5. ```python manage.py test``` にて/backend/rest_api/tests.py に記載されているテストが走る。
6. OK が出力されればテストが通っているので問題なし。



# ローカル開発のマイグレーションがうまく効かない時の対応法
- テーブル名の変更が効いていない可能性がある。
- マイグレーションファイルを消しても、テーブルが消えるわけではない
- Dockerのボリュームを消してあげないとだめ