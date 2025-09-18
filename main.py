import requests
import bs4
from datetime import datetime
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
worldnews = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWorldNews', headers=headers)
business = requests.get('https://feeds.content.dowjones.io/public/rss/WSJcomUSBusiness', headers=headers)
markets = requests.get('https://feeds.content.dowjones.io/public/rss/RSSMarketsMain', headers=headers)
tech = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWSJD', headers=headers)
economy = requests.get('https://feeds.content.dowjones.io/public/rss/socialeconomyfeed', headers=headers)

curr = business

curr.raise_for_status()
soup = bs4.BeautifulSoup(curr.content, 'xml')

output = []

for item in soup.find_all('item'):
    title_name = item.find('title').text
    title_day = (item.find('pubDate').text)
    title_weekday = title_day[:4]
    title_month = title_day[7:11]
    title_year = title_day[11:16]
    title_day = title_day[4:7]
    if title_month == " Sep":
        output.append([title_name, title_weekday, title_day, title_month, title_year])


output_sorted = sorted(output, key=lambda x: int(x[2]), reverse=True)

for x in output_sorted:
    print(x)