import datetime
import asyncio

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
article_cache = []

POLL_INTERVAL = 600  # 10 minutes


def fetch_and_cache():
    global article_cache

    cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=6)
    feeds_dict = scraper.fetch_all_feeds()

    all_articles = []
    for feed in feeds_dict.values():
        all_articles.extend(scraper.news_list(feed, tz, cutoff))

    all_articles = sorted(all_articles, reverse=True)

    article_cache = [
        {
            "title": a.title,
            "date": a.date.isoformat(),
            "link": a.link,
            "description": a.desc,
            "category": a.column,
        }
        for a in all_articles
    ]


async def poll_feeds():
    while True:
        fetch_and_cache()
        await asyncio.sleep(POLL_INTERVAL)


@app.on_event("startup")
async def startup():
    asyncio.create_task(poll_feeds())


@app.get("/api/articles")
def get_articles():
    return article_cache


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
