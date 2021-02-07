#!/usr/bin/env python3
import json
import os
import discord
from discord.ext import commands

import music

bot = commands.Bot(command_prefix='|', description="Daj eno zgodlej")

@bot.event
async def on_ready():
    activity = discord.Game(name='|play sampanjac')
    await bot.change_presence(activity=activity)
    print(f'Logged in as {bot.user.name}')
    bot.add_cog(music.Music(bot))

def main():
<<<<<<< HEAD
    #with open('config.json') as fh:
    #   bot.config = json.load(fh)
   
=======
    # with open('config.json') as fh:
    #     bot.config = json.load(fh)

    # bot.run(bot.config['token'])
>>>>>>> 205d6d352eaf74080ec7757ee9f761539b6c92e8
    bot.run(os.environ['token'])
    


if __name__ == "__main__":
    main()