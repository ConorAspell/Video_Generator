from datetime import datetime
import requests
import json
import os
import praw 
import time
from pystreamable import StreamableApi
from fake_useragent import UserAgent

def upload_to_streamable(path):
    username = os.environ.get("username")
    password = os.environ.get("password")
    api = StreamableApi(username, password)
    deets = api.upload_video(path, path.split('/')[-1])
    count = 0
    while True:
        count+=1
        test = api.get_info(deets['shortcode'])
        if test['percent'] == 100:
            break
        elif count == 6:
            exit()
        else:
            time.sleep(10)
    return "https://streamable.com/" +deets['shortcode']

def upload_to_reddit(url='https://streamable.com/6ws17r'):
    username = os.environ.get("username")
    password = os.environ.get("password")
    reddit_id = os.environ.get("reddit_id")
    reddit_secret = os.environ.get("reddit_secret")
    subreddit = os.environ.get("subreddit")"
    ua = UserAgent()
    user_agent = ua.random
    reddit = praw.Reddit(client_secret = reddit_secret,
    client_id = reddit_id,
    user_agent = user_agent,
    username=username,
    password=password
    )
    reddit.subreddit(subreddit).submit(title='Top Twitch Clips for This Week', url=url)