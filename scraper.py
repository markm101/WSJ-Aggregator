import bs4
from article import Article
import requests
import datetime
import time

def news_list(curr, timezone, limit_date):
    '''
    Returns a list of Article type variables describing the current articles present in the RSS feed of the requested column

    :note: If limit_date is not requested, it is passed as NONE, returning the entire content of the JSON

    :param curr: A response object of a specific column, giving the JSON data of the feed later converted to XML
    :param timezone: Requested timezone object by the user ( PST, EST or CST )
    :param limit_date: A limit date requested by the user
    '''
    output = []
    curr.raise_for_status()
    soup = bs4.BeautifulSoup(curr.content, 'xml')
    column = soup.find('channel').find('title').text

    #With each item found in curr (column), create a article object and store in the output variable
    #If the article's title is already in output, do not append it to output
    for item in soup.find_all('item'):
        new_art = Article(item.find('title').text.strip(), item.find('pubDate').text, item.find('link').text, column, timezone)
        if limit_date != None:
            if new_art.date > limit_date:
                if new_art not in output:
                    output.append(new_art)
        else:
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
    timeZone  = datetime.timezone(datetime.timedelta(hours=-5), 'EST')
    called_time = datetime.datetime.now(datetime.UTC).astimezone(timeZone)
    
    # sort curr_news by descending order (most recent article first)
    
    while True is True:  

        headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
        worldnews = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWorldNews', headers=headers)
        business = requests.get('https://feeds.content.dowjones.io/public/rss/WSJcomUSBusiness', headers=headers)
        markets = requests.get('https://feeds.content.dowjones.io/public/rss/RSSMarketsMain', headers=headers)
        tech = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWSJD', headers=headers)
        economy = requests.get('https://feeds.content.dowjones.io/public/rss/socialeconomyfeed', headers=headers)

        curr_news = sorted(news_list(worldnews, timeZone, called_time) + news_list(business, timeZone, called_time) + news_list(markets, timeZone, called_time) + news_list(tech, timeZone, called_time) + news_list(economy, timeZone, called_time), reverse=True)

        if curr_news == []:
            print(f' \n No new articles have been published between {called_time} and {datetime.datetime.now(datetime.UTC).astimezone(timeZone)}')
        else:
            print('\nNew articles found')
            for x in curr_news:
                print(str(x))
            print('\n')

        print(f'The refresh time will now be set to {called_time}')

                print('News is up to date')
        time.sleep(int(seconds))
    

