# Project Title

Wall Street Journal News Aggregate
## Description

A Wall Street Journal Aggregator that presents news articles in an easily accessible way using the Wall Street Journal RSS feed
By default all dates will be in Eastern Standard Time

## Getting Started

### Dependencies

This project requires BeautifulSoup4 for XML parsing and requests for fetching feeds.

### Installing

Clone the repository: git clone https://github.com/markm101/WSJ-Aggregator cd WSJ-Aggregator

Install Beautiful Soup and Requests: pip install beautifulsoup4 lxml requests

### Executing program

Adjust limit date within main.py
Run the mainscript to fetch the latest headlines:
```
python main.py
```

### Output Sample

The generated out.txt would look something like this
```
Global Markets Rally Amid Tech Surge    || 01/05/26 at 23:10 EST || Markets || https://wsj.com/articles/sample-link
```
## Authors

Mark M

## Version History

* 1.0
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

* [WSJ](WSJ.com)
* [MORSS](https://morss.it/)
