import datetime


class Article:
    def __init__(self, title, date, link, desc, column, timezone):
        """
        Docstring for __init__

        :param title: Title of the news article
        :param date: Date Published (string)
        :param link: Link to the article (string)
        :param desc: Brief description of the article
        :param column: The column // Type of article
        :param timezone: The user requested timezone in terms of output / storage
        """

        # Set article class variables
        self.title = title
        self.column = column
        self.link = link
        self.desc = desc

        # Sample: Mon, 05 Jan 2026 04:10:55 GMT (WSJ RSS Format)
        format_str = "%a, %d %b %Y %H:%M:%S %Z"

        # Stores the date as a datetime type
        # Places the original timezone as UTC and then converts (Ensures accurate date upon conversion)
        self.date = (
            datetime.datetime.strptime(date, format_str)
            .replace(tzinfo=datetime.timezone.utc)
            .astimezone(timezone)
        )
        self.timezone = timezone

    def __str__(self):
        return f"{self.title: <100} || {self.date.strftime('%x')} at {self.date.strftime('%X')[:5]} {self.timezone} || {self.column} \n {self.link} \n"

    def __gt__(self, other):
        return self.date > other.date

    def __lt__(self, other):
        return self.date < other.date

    def __eq__(self, other):
        return self.title == other.title

    def __ne__(self, other):
        return self.title != other.title
