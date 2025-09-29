import requests
import bs4
import datetime
from database import *
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
worldnews = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWorldNews', headers=headers)
business = requests.get('https://feeds.content.dowjones.io/public/rss/WSJcomUSBusiness', headers=headers)
markets = requests.get('https://feeds.content.dowjones.io/public/rss/RSSMarketsMain', headers=headers)
tech = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWSJD', headers=headers)
economy = requests.get('https://feeds.content.dowjones.io/public/rss/socialeconomyfeed', headers=headers)



month = datetime.datetime.now().strftime("%b")
day = datetime.datetime.now().strftime("%d")
def news_list(curr, column, choice):

    output = []
    added_headlines = []
    curr.raise_for_status()
    soup = bs4.BeautifulSoup(curr.content, 'xml')

    for item in soup.find_all('item'):
        title_name = item.find('title').text.strip()
        title_date = item.find('pubDate').text
        title_weekday = title_date[:4]
        title_month = title_date[8:11]
        title_year = title_date[11:16]
        title_day = title_date[5:7]
        title_hour = title_date[17:19]
    
        if (title_month == month) and (title_name not in added_headlines) and title_day == day:
            output.append([title_name, title_weekday, title_day, title_hour, title_month, title_year, column])
            add_articles(title_name, title_day, title_month, column, choice)
            added_headlines.append(title_name)

    articles = sorted(output, key=lambda x: int(x[3]), reverse=True)
    return (articles)
    



