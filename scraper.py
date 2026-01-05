import bs4
import datetime

class Article():
    def __init__(self, title, date, column):
        self.title = title
        self.column = column

        #Sample: Mon, 05 Jan 2026 04:10:55 GMT
        format_str = "%a, %d %b %Y %H:%M:%S %Z"
        #Adjust for GMT Timezone by subtracting five hour timedelta
        self.date = datetime.datetime.strptime(date, format_str) - datetime.timedelta(hours=5)

    def getDate(self):
        #Day, Month, Year
        return(self.date.strftime('%x'))
    
    def getColumn(self):
        return(self.column)
    
    def __str__(self):
        return (self.title + '  |||||||||  ' + self.getDate() + ' at ' + self.date.strftime('%X')[:5] + ' EST  |||||||||  ' + self.column)
    
    def __gt__(self, other):
        return self.date > other.date

def news_list(curr, limit_date=None):
    output = []
    curr.raise_for_status()
    soup = bs4.BeautifulSoup(curr.content, 'xml')
    column = soup.find('channel').find('title').text

    for item in soup.find_all('item'):
        new_art = Article(item.find('title').text.strip(), item.find('pubDate').text, column)
        if new_art.date < limit_date:
            break
        if new_art not in output:
            output.append(new_art)

    output = sorted(output)
    return (output)



