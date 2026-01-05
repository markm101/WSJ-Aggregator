import requests
from scraper import news_list
import datetime
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
worldnews = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWorldNews', headers=headers)
business = requests.get('https://feeds.content.dowjones.io/public/rss/WSJcomUSBusiness', headers=headers)
markets = requests.get('https://feeds.content.dowjones.io/public/rss/RSSMarketsMain', headers=headers)
tech = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWSJD', headers=headers)
economy = requests.get('https://feeds.content.dowjones.io/public/rss/socialeconomyfeed', headers=headers)

"""
            news_list(worldnews, "world news")
            news_list(business, "business")
            news_list(markets, "markets")
            news_list(tech, "tech")
            news_list(economy, "economy")
"""
def main():
    feeds = [worldnews, business, markets, tech, economy]
    for x in feeds:
        for y in news_list(x, datetime.datetime(2026, 1, 4) - datetime.timedelta(hours=5)):
            print(y)


if __name__ == "__main__":
    main()