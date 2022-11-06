#!/usr/local/bin/python3

import tweepy
import os
from dotenv import load_dotenv
load_dotenv(override=True)

# 認証情報は.envから取得する
API_KEY = os.getenv('API_KEY')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# 認証情報を元にクライアントを生成
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# 自身の情報を取得
resp = client.get_me()
my_name = resp.data.name

resp = client.create_tweet(
    text='python/tweepyでツイート'
)

print(f'{my_name}>{resp.data["text"]}')
