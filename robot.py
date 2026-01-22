import discord
from scraper import news_list
import requests
import datetime
import time


bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command()
async def start_feed(ctx, seconds):


    timeZone  = datetime.timezone(datetime.timedelta(hours=-5), 'EST')
    called_time = datetime.datetime.now(datetime.UTC).astimezone(timeZone)
    
    # sort curr_news by descending order (most recent article first)
    
    while True is True:  

        headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
        worldnews = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWorldNews', headers=headers)
        business = requests.get('https://feeds.content.dowjones.io/public/rss/WSJcomUSBusiness', headers=headers)
        markets = requests.get('https://feeds.content.dowjones.io/public/rss/RSSMarketsMain', headers=headers)
        tech = requests.get('https://feeds.content.dowjones.io/public/rss/RSSWSJD', headers=headers)
        economy = requests.get('https://feeds.content.dowjones.io/public/rss/socialeconomyfeed', headers=headers)

        curr_news = sorted(news_list(worldnews, timeZone, called_time) + news_list(business, timeZone, called_time) + news_list(markets, timeZone, called_time) + news_list(tech, timeZone, called_time) + news_list(economy, timeZone, called_time), reverse=True)

        if curr_news == []:
            await ctx.send(f'No new articles have been published between {called_time} and {datetime.datetime.now(datetime.UTC).astimezone(timeZone)}')
        else:
            await ctx.send('New articles found')
            for x in curr_news:
                my_embed = discord.Embed(title = x.title, description = x.desc, timestamp = x.date, type = x.column, color=0xFF0000)
                my_embed.add_field(name = 'Link', value = f'[Link]({x.link})', inline=False)
                await ctx.send('new article published', my_embed)

        called_time = datetime.datetime.now(datetime.UTC).astimezone(timeZone)
        await ctx.send(f'The refresh time will now be set to {called_time}')

        time.sleep(int(seconds))

