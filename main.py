import datetime

import scraper

if __name__ == "__main__":
    # Ask user for prefered timezone
    time_zone = input("1) PST   2) CST   3) EST\n")
    if time_zone == "1":
        time_zone = datetime.timezone(datetime.timedelta(hours=-8), "PST")
    elif time_zone == "2":
        time_zone = datetime.timezone(datetime.timedelta(hours=-6), "CST")
    elif time_zone == "3":
        time_zone = datetime.timezone(datetime.timedelta(hours=-5), "EST")
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
        names = ["World News", "Business", "Markets", "Tech", "Economy"]
        feeds = list(feeds_dict.values())

        with open("output.txt", "w", encoding="utf-8") as file:
            for i, feed in enumerate(feeds):
                file.writelines(f"\n ----- {names[i]} ----- \n \n")
                for article in scraper.news_list(feed, time_zone, date):
                    file.writelines(str(article) + "\n")

    elif master == "2":
        scraper.new_news(input("Time in between checks (seconds)\n"), time_zone)

    elif master == "3":
        scraper.discord_start(
            input("Enter Bot Token: \n"),
            input("Enter Gemini Token (Leave blank for none): \n"),
            time_zone,
        )
