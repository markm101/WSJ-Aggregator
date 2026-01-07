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
        timeZone = datetime.timezone(datetime.timedelta(hours=-8), 'PST')
    elif timeZone == '2':
        timeZone = datetime.timezone(datetime.timedelta(hours=-6), 'CST')
    elif timeZone == '3':
        timeZone  = datetime.timezone(datetime.timedelta(hours=-5), 'EST')
    else:
        timeZone = datetime.timezone.utc

    date = input('Limit Date? (format 2026-01-04)\n')
    try:
        date = datetime.datetime.fromisoformat(date).replace(tzinfo=timeZone)
    except:
        print('Not Limiting')
        date = None


    i = 0
    names = ["World News", "Business", "Markets", "Tech", "Economy"]
    feeds = [worldnews, business, markets, tech, economy]

    with open("out.txt", "w", encoding="utf-8") as file:
        for x in feeds:
            file.writelines(f'----- {names[i]} ----- \n')
            for y in news_list(x, timeZone, date):
                file.writelines(str(y) + '\n')
            i += 1