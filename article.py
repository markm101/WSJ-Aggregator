import datetime


class Article():
    def __init__(self, title, date, link, column, timezone):
        self.title = title
        self.column = column
        self.link = link

        #Sample: Mon, 05 Jan 2026 04:10:55 GMT
        format_str = "%a, %d %b %Y %H:%M:%S %Z"
        self.date = datetime.datetime.strptime(date, format_str).astimezone(timezone)
        self.timezone = timezone

    def getDate(self):
        #Day, Month, Year
        return(self.date.strftime('%x'))
    
    def getColumn(self):
        return(self.column)
    
    def __str__(self):
        return (f'{self.title: <82} || {self.getDate()} at {self.date.strftime('%X')[:5]} {self.timezone} || {self.column} || {self.link}')
    
    def __gt__(self, other):
        return self.date > other.date
    
    def __eq__(self, other):
        return self.title == other.title