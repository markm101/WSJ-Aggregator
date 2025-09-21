import requests
import bs4
import datetime
from parsing import news_list

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
worldnews = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWorldNews', headers=headers)
business = requests.get('https://feeds.content.dowjones.io/public/rss/WSJcomUSBusiness', headers=headers)
markets = requests.get('https://feeds.content.dowjones.io/public/rss/RSSMarketsMain', headers=headers)
tech = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWSJD', headers=headers)
economy = requests.get('https://feeds.content.dowjones.io/public/rss/socialeconomyfeed', headers=headers)


i = 0

total = []
while i < 4:
    if i == 0:
        print("worldnews")
        total += news_list(worldnews)
    elif i == 1:
        print("business")
        total += news_list(business)
    elif i == 2:
        print("markets")
        total += news_list(markets)
    elif i == 3:
        print("tech")
        total += news_list(tech)
    elif i == 4:
        print("economy")
        total += news_list(economy)

    i += 1

print(total)
        
