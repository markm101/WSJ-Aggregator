import bs4
from article import Article

def news_list(curr, timezone, limit_date):
    output = []
    curr.raise_for_status()
    soup = bs4.BeautifulSoup(curr.content, 'xml')
    column = soup.find('channel').find('title').text

    for item in soup.find_all('item'):
        new_art = Article(item.find('title').text.strip(), item.find('pubDate').text, item.find('link').text, column, timezone)
        if limit_date != None:
            if new_art.date < limit_date:
                break
        if new_art not in output:
            output.append(new_art)

    output = sorted(output)
    return (output)



