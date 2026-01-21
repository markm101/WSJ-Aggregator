import discord
import scraper
import requests
import datetime



bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command()
async def get_output(ctx):
    timeZone  = datetime.timezone(datetime.timedelta(hours=-5), 'EST')
    date = datetime.datetime.fromisoformat('2026-01-15').replace(tzinfo=timeZone)

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    worldnews = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWorldNews', headers=headers)
    business = requests.get('https://feeds.content.dowjones.io/public/rss/WSJcomUSBusiness', headers=headers)
    markets = requests.get('https://feeds.content.dowjones.io/public/rss/RSSMarketsMain', headers=headers)
    tech = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWSJD', headers=headers)
    economy = requests.get('https://feeds.content.dowjones.io/public/rss/socialeconomyfeed', headers=headers)

    names = ["World News", "Business", "Markets", "Tech", "Economy"]
    feeds = [worldnews, business, markets, tech, economy]
    i=0
    output = []
    for x in feeds:
        await ctx.send(f'\n ----- {names[i]} ----- \n \n')
        for y in scraper.news_list(x, timeZone, date):
            await ctx.send(str(y) + '\n')
        i += 1

bot.run('')