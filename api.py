import datetime
import asyncio
from contextlib import asynccontextmanager
from zoneinfo import ZoneInfo

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import scraper


tz = ZoneInfo("America/New_York")
article_cache = []
last_fetched = None

POLL_INTERVAL = 900  # 15 minutes


def fetch_and_cache():
    global article_cache, last_fetched

    expiry = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=3)

    try:
        # Every poll reads the full 3 days, so a failed poll can't cost any articles
        parsed = scraper.parse_feeds(scraper.fetch_all_feeds(), tz, expiry)

        if not parsed:
            print("No feeds available, keeping cached articles")
            return

        # Merge into copies, so requests never read an entry mid-update
        merged = {a["guid"]: {**a} for a in article_cache}
        for articles in parsed.values():
            for a in articles:
                entry = merged.setdefault(a.guid, {"guid": a.guid, "date": "", "category": ""})

                # A later date means WSJ updated the article, so show the new version
                if a.date.isoformat() > entry["date"]:
                    entry.update(
                        title=a.title,
                        date=a.date.isoformat(),
                        link=a.link,
                        description=a.desc,
                    )

                # Stays one string so open tabs and saved browser data keep working
                if a.column not in entry["category"]:
                    entry["category"] = f"{entry['category']}, {a.column}".removeprefix(", ")

        # Remove articles older than 3 days
        article_cache = [
            a for a in merged.values()
            if datetime.datetime.fromisoformat(a["date"]) > expiry
        ]

        article_cache = sorted(article_cache, key=lambda a: a["date"], reverse=True)
        last_fetched = datetime.datetime.now(tz).isoformat()
    except Exception as e:
        print(f"Failed to fetch feeds: {e}")


async def poll_feeds():
    while True:
        await asyncio.sleep(POLL_INTERVAL)
        try:
            await asyncio.to_thread(fetch_and_cache)
        except Exception as e:
            print(f"Polling error: {e}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Later polls run in the background, but the first one has to finish before pages can load
    await asyncio.to_thread(fetch_and_cache)
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
