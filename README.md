# Wall Street Journal News Aggregate

## Description

A Wall Street Journal Aggregator that presents newly published news articles in an easily accessible way using the Wall Street Journal RSS feed

## Getting Started

### Dependencies

This project requires BeautifulSoup4 for XML parsing and requests for fetching feeds.

### Installing

Clone the repository: git clone https://github.com/markm101/WSJ-Aggregator cd WSJ-Aggregator

Install Beautiful Soup and Requests: pip install beautifulsoup4 requests

### Executing program

Adjust limit date within main.py
Run the mainscript to write the latest headlines to out.txt:
User selects the timezone and a limit date (blank if no limit date is needed)
```
python main.py
```

### Output Sample

The generated out.txt would look something like this
```
Global Markets Rally Amid Tech Surge    || 01/05/26 at 23:10 EST || Markets || https://wsj.com/articles/sample-link
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

* [WSJ](WSJ.com)
* [MORSS](https://morss.it/)
