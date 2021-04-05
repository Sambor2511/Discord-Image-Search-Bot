import discord
from discord.ext import commands
import os
from googleapiclient.discovery import build

#! Import this
import random

client = commands.Bot(command_prefix="$")
api_key = "<YOUR CUSTOM SEARCH API KEY>"


@client.event
async def on_ready():
    print("!!! Bot Is Online !!!\n")


@client.command(aliases=["show"])
async def showpic(ctx, *, search):
    ran = random.randint(0, 9)
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    result = resource.list(
        q=f"{search}", cx="<YOUR SEARCH ENGINE ID>", searchType="image"
    ).execute()
    url = result["items"][ran]["link"]
    embed1 = discord.Embed(title=f"Here Your Image ({search.title()})")
    embed1.set_image(url=url)
    await ctx.send(embed=embed1)


client.run("<YOUR DISCORD BOT TOKEN>")
