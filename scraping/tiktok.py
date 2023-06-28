'''
This file scrapes from Tiktok using the TikTokApi library
Which can be accessed at https://github.com/davidteather/TikTok-Api
The tool requires cookies of a registered user which I've put into cookies.json
We will be extracting information from the trending page of the app
'''
from TikTokApi import TikTokApi
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

with open('tiktok-data/data.json', 'w') as f:
    with TikTokApi() as api:
        api._get_cookies = get_cookies
        for trending_video in api.trending.videos():
            f.write(json.dumps(trending_video.as_dict))
            f.write('\n')

f.close()