import bs4
from article import Article
import requests
import datetime
import time

def news_list(curr, timezone, limit_date):
    output = []
    curr.raise_for_status()
    soup = bs4.BeautifulSoup(curr.content, 'xml')
    column = soup.find('channel').find('title').text

    for item in soup.find_all('item'):
        new_art = Article(item.find('title').text.strip(), item.find('pubDate').text, item.find('link').text, column, timezone)
        if limit_date != None:
            if new_art.date < limit_date:
                break
        if new_art not in output:
            output.append(new_art)

    
    output = sorted(output)
    return (output)

def new_news(seconds, timeZone):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    worldnews = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWorldNews', headers=headers)
    business = requests.get('https://feeds.content.dowjones.io/public/rss/WSJcomUSBusiness', headers=headers)
    markets = requests.get('https://feeds.content.dowjones.io/public/rss/RSSMarketsMain', headers=headers)
    tech = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWSJD', headers=headers)
    economy = requests.get('https://feeds.content.dowjones.io/public/rss/socialeconomyfeed', headers=headers)
    """
    Curr_news a list of article classes of every single article in the RSS feed
    Prints new news articles in the console on a x minute interval
    """
    timeZone  = datetime.timezone(datetime.timedelta(hours=-5), 'EST')
    # sort curr_news by descending order (most recent article first)
    curr_news =  sorted(news_list(worldnews, timeZone, None) + news_list(business, timeZone, None) + news_list(markets, timeZone, None) + news_list(tech, timeZone, None) + news_list(economy, timeZone, None), reverse=True)
    while True is True:
        new_news = sorted(news_list(worldnews, timeZone, None) + news_list(business, timeZone, None) + news_list(markets, timeZone, None) + news_list(tech, timeZone, None) + news_list(economy, timeZone, None), reverse=True)
        i = 0
        while i < len(curr_news):
            if curr_news[i] != new_news[i]:
                print(str(new_news[i]))
                i += 1
            else:
                print('News is up to date')
                break
        time.sleep(int(seconds))
    

