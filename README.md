# サンプル（プロダクト名）

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2022/08/JPHACKS2022_ogp.jpg)](https://www.youtube.com/watch?v=LUPQFB4QyVo)

## 製品概要
### 背景(製品開発のきっかけ、課題等）
### 製品説明（具体的な製品の説明）
### 特長
#### 1. 特長1
#### 2. 特長2
#### 3. 特長3

### 解決出来ること
### 今後の展望
### 注力したこと（こだわり等）
* 
* 

## 開発技術
### 活用した技術
#### API・データ
* 
* 

#### フレームワーク・ライブラリ・モジュール
* 
* 

#### デバイス
* 
* 

### 独自技術
#### ハッカソンで開発した独自機能・技術
* 独自で開発したものの内容をこちらに記載してください
* 特に力を入れた部分をファイルリンク、またはcommit_idを記載してください。

#### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）
* 
* 



# バックエンド
### セットアップできているかの確認作業
1. `make dc/up-build`でコンテナ作成
2. `cd backend && make ls-docker-db`バックエンドに移動してデータベースの確認をする。`\l`で`sokuseki_db`dbが作成されているか確認
3. adminURL`http://localhost:8000/admin/`でログインページでたらOK


```mermaid
erDiagram

users {
    integer user_id PK
    string user_name
    string address
    string password
}

users_communities {
    integer id PK
    integer community_id FK
    integer user_id FK
}

communities {
    integer community_id PK
    string cummunity_name
} 

articles {
    integer article_id  PK
    string article_name 
    string article_content
    datetime meeting_time
    datetime created_at
}
article_community {
    integer article_id FK
    integer community_id FK
}

articles ||--o{article_community:""
communities ||--o{article_community:""

users ||--o{users_communities:""
communities ||--o{users_communities:""



```


## API 
- /users/create POST ユーザ名を作成する
- /users/:id       GET ユーザ情報を取得
- /users/:id/update PUT ユーザ情報更新
- /users/:id/articles GET ユーザが投稿した料理一覧
- /users/:id/articles/:article_id GET ユーザが投稿した料理
- /community/create POST コミュニティ作成
- /community/:id    GET コミュニティを取得
- /community/:id/users GET 参加する人(数)