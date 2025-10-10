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


def update_list(choice): 
    '''
        Updates the list of a given choice with the most recent news articles       
        Instead of restarting the lists every time, append to the lists
        Plan : Reset the list every few days for easier storage
    '''
    i = 0
    total = []
    make_table(choice)
    while i < 4:
        if i == 0:
            news_list(worldnews, "world news", choice)
        elif i == 1:
            news_list(business, "business", choice)
        elif i == 2:
            news_list(markets, "markets", choice)
        elif i == 3:
            news_list(tech, "tech", choice)
        elif i == 4:
            news_list(economy, "economy", choice)

        i += 1


def find_updates(choice):
    '''
        Given the most recently updated choice, find the most recent updates to the news
        uses get_latestID and get_headline
        Compares the latest id of the updated list to the previous list, if its greater that means theres more elements and therefore newer articles
        TEST FOR BUGS         TEST FOR BUGS         TEST FOR BUGS         TEST FOR BUGS 
    '''
    out = []
    if choice == 1:
        i = get_latestID(1)
        while i > 0:
            if i > get_latestID(2):
                print(get_headline(i, 1))


    if choice == 2:
        i = get_latestID(2)
        while i > 0:
            if i > get_latestID(1):
                print(get_headline(i, 2))



choice = 1
update_list(1)
all_articles(1)

choice = 2
update_list(2)
print("updated")
all_articles(2)





# Make a compare tables function next, 