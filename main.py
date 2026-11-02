import datetime
from zoneinfo import ZoneInfo

import scraper

if __name__ == "__main__":
    # Ask user for preferred timezone
    time_zone = input("1) Pacific   2) Central   3) Eastern\n")
    if time_zone == "1":
        time_zone = ZoneInfo("America/Los_Angeles")
    elif time_zone == "2":
        time_zone = ZoneInfo("America/Chicago")
    elif time_zone == "3":
        time_zone = ZoneInfo("America/New_York")
    else:
        time_zone = datetime.timezone.utc

    # Main Option
    master = input(
        "Select Mode: 1) Standard output.txt print 2) Console Print new articles published 3)Discord + AI Mode \n"
    )
    if master == "1":
        date = input("Limit Date? (format 2026-01-04)\n")
        try:
            date = datetime.datetime.fromisoformat(date).replace(tzinfo=time_zone)
        except ValueError:
            print("Not Limiting")
            date = None

        print("Fetching feeds...")
        feeds_dict = scraper.fetch_all_feeds()
        names = {
            "worldnews": "World News",
            "business": "Business",
            "markets": "Markets",
            "tech": "Tech",
            "economy": "Economy",
        }

        with open("output.txt", "w", encoding="utf-8") as file:
            for name, articles in scraper.parse_feeds(feeds_dict, time_zone, date).items():
                file.writelines(f"\n ----- {names[name]} ----- \n \n")
                for article in articles:
                    file.writelines(str(article) + "\n")

    elif master == "2":
        scraper.new_news(input("Time in between checks (seconds)\n"), time_zone)

    elif master == "3":
        scraper.discord_start(
            input("Enter Bot Token: \n"),
            input("Enter Gemini Token (Leave blank for none): \n"),
            time_zone,
        )
