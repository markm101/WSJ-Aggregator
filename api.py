import datetime
import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import scraper


tz = datetime.timezone(datetime.timedelta(hours=-5), "EST")
article_cache = []
last_fetched = None

POLL_INTERVAL = 600  # 10 minutes


def fetch_and_cache():
    global article_cache, last_fetched

    now = datetime.datetime.now(datetime.timezone.utc)
    cutoff = now - datetime.timedelta(hours=6)
    expiry = now - datetime.timedelta(days=3)

    try:
        feeds_dict = scraper.fetch_all_feeds()

        all_articles = []
        for feed in feeds_dict.values():
            try:
                all_articles.extend(scraper.news_list(feed, tz, cutoff))
            except Exception as e:
                print(f"Failed to parse feed: {e}")

        # Merge new articles into cache, avoiding duplicates by title
        existing_titles = {a["title"] for a in article_cache}
        for a in all_articles:
            if a.title not in existing_titles:
                article_cache.append({
                    "title": a.title,
                    "date": a.date.isoformat(),
                    "link": a.link,
                    "description": a.desc,
                    "category": a.column,
                })
                existing_titles.add(a.title)

        # Remove articles older than 3 days
        article_cache = [
            a for a in article_cache
            if datetime.datetime.fromisoformat(a["date"]) > expiry
        ]

        article_cache = sorted(article_cache, key=lambda a: a["date"], reverse=True)
        last_fetched = datetime.datetime.now(tz).isoformat()
    except Exception as e:
        print(f"Failed to fetch feeds: {e}")


async def poll_feeds():
    while True:
        fetch_and_cache()
        await asyncio.sleep(POLL_INTERVAL)


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(poll_feeds())
    yield


app = FastAPI(title="WSJ Aggregator", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/api/articles")
def get_articles():
    return {"articles": article_cache, "last_fetched": last_fetched}


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
