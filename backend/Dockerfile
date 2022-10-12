# 公式からpython3.7 on alpine linuxイメージをpull
FROM python:alpine
# 作業ディレクトリを設定
WORKDIR /usr/src/backend



# 環境変数を設定
# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1

# psycopg2のインストール
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

RUN pip install --upgrade pip 

COPY . /usr/src/backend
RUN pip install -r requirements.txt

