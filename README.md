# slack_sqldb

## Overview
Langchainの SQLDatabaseChainを利用し、Databricksのデータに対して自然言語で問い合わせができます。またSlackを利用して問い合わせを出来るようになります。

## Requirement
- Databricks SQLWarehouse　　
- OpenAI API (Secret Keyが必要です）
- Slack App
- EC2 or Lamdaなど pythonコードが動作する環境。デモの場合はPCでも可能です。

## Usage
設定方法は、こちらのQiita記事をご覧ください。<br>
[Databricksのデータに SQLDatabaseChainを使ってSlackからアクセスしてみた](https://qiita.com/maroon-db/ed862592efb65b06d2a9)

## Features
OpenAI APIを利用した自然言語での日本語チャットが可能。
Databricksのデータに対して問い合わせが出来る
Slackをユーザーインターフェースにしている

## Reference
[LangchainのSQLDatabaseチェーンを使ってDatabricksのデータベースを操作する](https://qiita.com/taka_yayoi/items/164d195efb5e2625b832) (@taka_yayoi)

## Author
Junichi Maruyama
https://qiita.com/maroon-db

