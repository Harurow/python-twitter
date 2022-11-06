# Pythonつかって Twitter でつぶやく

## 用途

タイトル通りpythonを利用してtwitterでtweetします

## 準備

* pythonが利用できる環境
* `tweepy`が利用できる環境
* `dotenv`が利用できる環境
* TwitterAPI認証情報

### `tweepy`,`dotenv`について

`tweepy`,`dotenv`を利用しているので事前に`pip`または`pip3`でインストールが必要です

```sh
# 例
pip install tweepy dotenv
```

### TwitterAPI認証情報について

Twitterを外部から利用する場合、認証情報が別途必要です。
必要に応じて別途発行してください。必要な情報は、

* API_KEY
* API_KEY_SECRET
* ACCESS_TOKEN
* ACCESS_TOKEN_SECRET

となります。

セキュリティの関係上、今回のコードには記載しておらず
`.env`ファイルに以下のような形で記載しています。

```sh:.env
API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxx"
API_KEY_SECRET="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
ACCESS_TOKEN="0000000000000000000-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
ACCESS_TOKEN_SECRET="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
また`.gitignore`で`.env`を追加しているので`git`の追跡対象外にしています。

### 注意事項

twitterでは同じ発言を連続でしようとするとエラーが発生します。
その仕様の為このコードは連続で実行すると2回目以降は失敗します。
時間を空けるか送信内容のメッセージを変更する必要があります。
