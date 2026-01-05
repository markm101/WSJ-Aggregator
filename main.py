import requests
from scraper import news_list
import datetime

if __name__ == "__main__":
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    worldnews = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWorldNews', headers=headers)
    business = requests.get('https://feeds.content.dowjones.io/public/rss/WSJcomUSBusiness', headers=headers)
    markets = requests.get('https://feeds.content.dowjones.io/public/rss/RSSMarketsMain', headers=headers)
    tech = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWSJD', headers=headers)
    economy = requests.get('https://feeds.content.dowjones.io/public/rss/socialeconomyfeed', headers=headers)

    timeZone = input('1) PST   2) CST   3) EST\n')
    if timeZone == '1':
        timeZone = datetime.timezone(datetime.timedelta(hours=-18), 'PST')
    if timeZone == '2':
        timeZone = datetime.timezone(datetime.timedelta(hours=-12), 'CST')
    if timeZone == '3':
        timeZone  = datetime.timezone(datetime.timedelta(hours=-10), 'EST')

    date = input('Date? (format 2026-01-04)\n')
    format_str = "%m-%d-$Y"
    date = datetime.datetime.fromisoformat(date).astimezone(timeZone)



    final = []
    feeds = [worldnews, business, markets, tech, economy]
    for x in feeds:
        '''
        for y in news_list(x, datetime.datetime(2026, 1, 4) - datetime.timedelta(hours=5)):
            final.append(str(y) + '\n')
            '''
        for y in news_list(x, timeZone, date):
            final.append(str(y) + '\n')

    with open("out.txt", "w", encoding='utf-8') as file:
        file.writelines(final)