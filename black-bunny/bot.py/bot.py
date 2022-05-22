import discord
from discord.ext import commands

bot=commands.Bot(command_preFix='~')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('ODc4ODAwOTE4OTk5NjA1MjY4.GCy-7s.gT5lzg9akSuL1rKK_ALquG2_a5Kn1K1cLzinog')