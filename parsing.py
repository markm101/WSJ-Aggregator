import requests
import bs4
import datetime
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
worldnews = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWorldNews', headers=headers)
business = requests.get('https://feeds.content.dowjones.io/public/rss/WSJcomUSBusiness', headers=headers)
markets = requests.get('https://feeds.content.dowjones.io/public/rss/RSSMarketsMain', headers=headers)
tech = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWSJD', headers=headers)
economy = requests.get('https://feeds.content.dowjones.io/public/rss/socialeconomyfeed', headers=headers)



month = datetime.datetime.now().strftime("%b")
day = datetime.datetime.now().strftime("%d")



class article():
    def __init__(self, title, date):
        self.title = title
        self.fulldate = date
        self.day = date[5:8] 
        self.month = date[8:11] 
        self.year = date[11:16]
        self.weekday = date[:4]
        self.hour = date[17:19]
    def getDate(self):
        #Day, Month, Year
        return(self.day + self.month + self.year)
    def getHour(self):
        return(self.hour)
    def __str__(self):
        return (self.title + ' on ' + self.getDate() + ' at ' + self.getHour())
    
    def __gt__(self, other):
        month_dict = {"Jan": 1,
                      "Feb": 2,
                      "Mar": 3,
                      "Apr": 4,
                      "May": 5,
                      "Jun": 6,
                      "Jul": 7,
                      "Aug": 8,
                      "Sep": 9,
                      "Oct": 10,
                      "Nov": 11,
                      "Dec": 12}
        if month_dict[self.month] == month_dict[other.month]:
            if self.day == other.day:
                if self.hour >= other.hour:
                    return True
            elif self.day > other.day:
                return True
        elif month_dict[self.month] < month_dict[other.month]:
            if self.month == "Jan" and other.month == "Dec":
                return True
            else:
                return False
        else:
            return False



    #title_month = title_date[8:11]
    #title_year = title_date[11:16]
    #title_day = title_date[5:7]
    #title_hour = title_date[17:19]

def news_list(curr, column):

    output = []
    curr.raise_for_status()
    soup = bs4.BeautifulSoup(curr.content, 'xml')

    for item in soup.find_all('item'):
        new_art = article(item.find('title').text.strip(), item.find('pubDate').text)
        if new_art not in output:
            output.append(new_art)
        '''
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
    '''
    output = sorted(output)
    return ([column, ] + output)
    



