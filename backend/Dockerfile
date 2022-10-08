# 公式からpython3.7 on alpine linuxイメージをpull
FROM python:alpine
# 作業ディレクトリを設定
WORKDIR /usr/src/backend



# 環境変数を設定
# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1
# Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1

# psycopg2のインストール
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

RUN pip install --upgrade pip \
    && pip install pipenv

# ホストのpipfileをコンテナの作業ディレクトリにコピー
COPY ./Pipfile /usr/src/backend/Pipfile

# pipfileからパッケージをインストールしてDjango環境を構築
RUN pipenv install --skip-lock --system --dev

COPY . /usr/src/backend