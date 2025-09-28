import requests
import bs4
import datetime
from parsing import news_list
from database import *
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
worldnews = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWorldNews', headers=headers)
business = requests.get('https://feeds.content.dowjones.io/public/rss/WSJcomUSBusiness', headers=headers)
markets = requests.get('https://feeds.content.dowjones.io/public/rss/RSSMarketsMain', headers=headers)
tech = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWSJD', headers=headers)
economy = requests.get('https://feeds.content.dowjones.io/public/rss/socialeconomyfeed', headers=headers)


selected == 2


def update_list():
    i = 0
    total = []
    make_table()
    while i < 4:
        if i == 0:
            news_list(worldnews, "world news")
        elif i == 1:
            news_list(business, "business")
        elif i == 2:
            news_list(markets, "markets")
        elif i == 3:
            news_list(tech, "tech")
        elif i == 4:
            news_list(economy, "economy")

        i += 1

update_list()
all_articles()
