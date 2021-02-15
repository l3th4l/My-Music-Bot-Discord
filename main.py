#!/usr/bin/env python3
import json
import os
import discord
from discord.ext import commands

import music

bot = commands.Bot(command_prefix=':', description="Hello")

@bot.event
async def on_ready():
    activity = discord.Game(name='playing with music')
    await bot.change_presence(activity=activity)
    print(f'Logged in as {bot.user.name}')
    bot.add_cog(music.Music(bot))

def main():
    with open('config.json') as fh:
        bot.config = json.load(fh)

    bot.run(bot.config['token'])
    # bot.run(os.environ['token'])
    


if __name__ == "__main__":
    main()