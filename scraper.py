import bs4
from article import Article
import requests
import datetime
import time

def news_list(curr, timezone, limit_date):
    '''
    Returns a list of Article type variables describing the current articles present in the RSS feed of the requested column

    :note: If limit_date is not requested, it is passed as NONE, returning the entire content of the XML file

    :param curr: A response object of a specific column, giving the XML data of the feed
    :param timezone: Requested timezone object by the user ( PST, EST or CST )
    :param limit_date: A limit date requested by the user
    '''
    output = []
    curr.raise_for_status()
    soup = bs4.BeautifulSoup(curr.content, 'xml')
    column = soup.find('channel').find('title').text

    #With each item found in curr (column), create a article object and store in the output variable
    for item in soup.find_all('item'):
        new_art = Article(item.find('title').text.strip(), item.find('pubDate').text, item.find('link').text, column, timezone)
        if limit_date != None:
            if new_art.date < limit_date:
                break
        #If the article's title is already in output, do not append it to output
        if new_art not in output:
            output.append(new_art)

    # Sorts output based on date, from oldest date to newest date
    output = sorted(output)
    return (output)

def new_news(seconds, timeZone):
    '''
    Checks for new news stored in every RSS feed
    If new news is found, returns the new article to the console
    
    :param seconds: How often the function rechecks for new articles
    :param timeZone: Requested timezone by the user
    '''
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    worldnews = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWorldNews', headers=headers)
    business = requests.get('https://feeds.content.dowjones.io/public/rss/WSJcomUSBusiness', headers=headers)
    markets = requests.get('https://feeds.content.dowjones.io/public/rss/RSSMarketsMain', headers=headers)
    tech = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWSJD', headers=headers)
    economy = requests.get('https://feeds.content.dowjones.io/public/rss/socialeconomyfeed', headers=headers)


    timeZone  = datetime.timezone(datetime.timedelta(hours=-5), 'EST')
    # sort curr_news by descending order (most recent article first)
    curr_news =  sorted(news_list(worldnews, timeZone, None) + news_list(business, timeZone, None) + news_list(markets, timeZone, None) + news_list(tech, timeZone, None) + news_list(economy, timeZone, None), reverse=True)
    while True is True:

        #Fetches the XML feeds (might get rate limited, will have to recheck overnight **)
        worldnews = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWorldNews', headers=headers)
        business = requests.get('https://feeds.content.dowjones.io/public/rss/WSJcomUSBusiness', headers=headers)
        markets = requests.get('https://feeds.content.dowjones.io/public/rss/RSSMarketsMain', headers=headers)
        tech = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWSJD', headers=headers)
        economy = requests.get('https://feeds.content.dowjones.io/public/rss/socialeconomyfeed', headers=headers)



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
    

