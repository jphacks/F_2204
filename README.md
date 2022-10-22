# Yoriai

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2022/08/JPHACKS2022_ogp.jpg)](https://www.youtube.com/watch?v=LUPQFB4QyVo)

## 製品概要
### 背景(製品開発のきっかけ、課題等）
  - 日常的に料理やお菓子を作るが他の人に食べてもらう機会は少ない
  - 「自分から食べて!」と頼むのはなかなか
  - コロナが落ち着いてきたとはいえ、友達やコミュニティ同士のつながりが前に比べると薄い
  - 毎度外食すると金銭的な負担が大きい
  - 大学生や新社会人などは宅飲みなどで仲良くなることが多い
  - 毎度今日の予定どう？って聞くのはめんどくさい上に聞いた人に断られると次の人に聞く必要がある
  
### 製品説明（具体的な製品の説明）
料理を作る人(以降:募集者)がいまからこんなのつくります!というのを宣言することで、その人と同じコミュニティに参加している人に通知が送られる。  
その通知に対して、「行く」と返事するとその人の住所と何時ごろに出来上がるかを確認でき、実際に参加する人(以降:参加者)だけのチャットが表示される。  
またチャットの中で募集者が買ってきて欲しいもの(飲み物とか調味料など)が表示されており、参加者はこれを自分買っていきますなどを話したりすることができる。  
### 特長
#### 1. 特長1
コミュニティを選ぶだけで、いちいち個人的に誘う必要がない
#### 2. 特長2
何時ごろに出来上がるなどがわかるので、細かい時間を設定する必要がない
#### 3. 特長3
店などで食べたりしないので、金銭的な負担も少ない
#### 4. 特徴4
コミュニティ外の人には募集は表示されないので知らない人同士がくっつくことはなく、気まずいなどが起こらない。
#### 5. 特長5
料理以外にもイベントなどの募集にも使える(拡張性)


### 解決出来ること
- コロナ禍でのコミュニティのつながりの薄さを解消できる
- だれを誘うかや何時にどうするなどの細かい予定を立てる手間を省くことができる
- 募集者は料理などに集中するだけでよく、追加で必要な飲み物なども表示されるので、来る人も募集者になにいるー？とかを聞く手間を省くことができる

### 現在完成している部分
- 必要なAPIの実装
- AWS EC2上での公開の準備
- いくつかのUnit Test

### 今後の展望
- ユーザー認証機能の実装
- mapAPIなどの用いたUIの実装  
- リアルタイムでのチャット機能  
<!-- ### 注力したこと（こだわり等）
* 
*  -->

## 開発技術
- バックエンド・インフラ
  - python
    - Django
  - AWS
  - postgresql
- フロント
  - React
<!-- ### 活用した技術 -->
<!-- #### API・データ
* 
*  -->

#### フレームワーク・ライブラリ・モジュール
* Django
* Next.js

<!-- ### 独自技術
#### ハッカソンで開発した独自機能・技術
* 独自で開発したものの内容をこちらに記載してください
* 特に力を入れた部分をファイルリンク、またはcommit_idを記載してください。 -->

<!-- #### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）
* 
*  -->



# DB

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
    string uri
    string article_content
    integer community_id FK
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


