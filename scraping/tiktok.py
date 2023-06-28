'''
This file scrapes from Tiktok using the TikTokApi library
Which can be accessed at https://github.com/davidteather/TikTok-Api
The tool requires cookies of a registered user which I've put into cookies.json
We will be extracting information from the trending page of the app

'''
from TikTokApi import TikTokApi
from flatten_json import flatten
import pandas as pd
import json

def get_cookies_from_file():
    with open('scraping/cookies.json') as f:
        cookies = json.load(f)

    cookies_kv = {}
    for cookie in cookies:
        cookies_kv[cookie['name']] = cookie['value']

    return cookies_kv

cookies = get_cookies_from_file()

def get_cookies(**kwargs):
    return cookies

videos = []
with TikTokApi() as api:
    api._get_cookies = get_cookies
    for trending_video in api.trending.videos():
        video_data = flatten(trending_video.as_dict)

        for key in list(video_data.keys()):
            if 'challenge' in key or 'duet' in key or 'sticker' in key or 'avatar' in key or 'url' in key.lower() or 'cover' in key.lower() or 'textExtra' in key or 'Addr' in key or 'subtitleInfos' in key:
                del video_data[key]
        videos.append(video_data)

    df = pd.DataFrame.from_dict(videos)
    df.to_csv('tiktok-data/tiktok.csv', mode='a', index=False)
