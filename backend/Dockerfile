# 公式からpython3.7 on alpine linuxイメージをpull
FROM python:3.8

# 作業ディレクトリを設定
WORKDIR /usr/src/backend

# 環境変数を設定
# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1
# Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip \
    && pip install pipenv

# ホストのpipfileをコンテナの作業ディレクトリにコピー
COPY ./Pipfile /usr/src/backend/Pipfile

# pipfileからパッケージをインストールしてDjango環境を構築
RUN pipenv install --skip-lock --system --dev

COPY . /usr/src/backend