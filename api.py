import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import scraper


app = FastAPI(title="WSJ Aggregator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

tz = datetime.timezone(datetime.timedelta(hours=-5), "EST")
last_checked = datetime.datetime.now(datetime.UTC)

@app.get("/api/articles")
def get_articles():
    global last_checked

    feeds_dict = scraper.fetch_all_feeds()

    all_articles = []
    for feed in feeds_dict.values():
        all_articles.extend(scraper.news_list(feed, tz, last_checked))

    last_checked = datetime.datetime.now(datetime.UTC)

    result = []
    for a in all_articles:
        result.append({
            "title": a.title,
            "date": a.date.isoformat(),
            "link": a.link,
            "description": a.desc,
            "category": a.column,
        })

    return result
