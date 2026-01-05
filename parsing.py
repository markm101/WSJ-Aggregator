import requests
import bs4
import datetime
from datetime import timedelta






class article():
    def __init__(self, title, date):
        self.title = title
        #Sample: Mon, 05 Jan 2026 04:10:55 GMT
        format_str = "%a, %d %b %Y %H:%M:%S %Z"
        #Adjust for GMT Timezone by subtracting five hour timedelta
        self.date = datetime.datetime.strptime(date, format_str) - timedelta(hours=5)
    def getDate(self):
        #Day, Month, Year
        return(self.date.strftime('%x'))
    def __str__(self):
        return (self.title + '  |||||||||  ' + self.getDate() + ' at ' + self.date.strftime('%X')[:5] + ' EST ')
    
    def __gt__(self, other):
        return self.date > other.date


def news_list(curr, column):

    output = []
    curr.raise_for_status()
    soup = bs4.BeautifulSoup(curr.content, 'xml')

    for item in soup.find_all('item'):
        new_art = article(item.find('title').text.strip(), item.find('pubDate').text)
        if new_art not in output:
            output.append(new_art)

    output = sorted(output)
    return ([column, ] + output)
    



