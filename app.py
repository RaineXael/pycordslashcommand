import discord
import dotenv
import os
import logging
import sys

try:
    is_debug = sys.argv[1] == "-d"
except:
    is_debug = False

dotenv.load_dotenv()
bot = discord.Bot()

#init logger
logger = logging.getLogger('discord')
if is_debug:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.WARN)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
print("Logger done")

#import features for the bot
from songoftheday import SongOfTheDay
song_of_the_day = SongOfTheDay()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    logger.info(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")


math = discord.SlashCommandGroup("math", "Math related commands")

@math.command(name = "add", description =  "Add two numbers together")
async def mathadd(ctx, num1: int, num2: int):
    await ctx.respond(f"The answer is {num1+num2}!")

@math.command(name = "subtract", description = "Subtract two numbers together")
async def mathsub(ctx, num1: int, num2: int):
    await ctx.respond(f"The answer is {num1-num2}!")

@math.command(name = "multiply", description = "Multiply two numbers together")
async def mathmult(ctx, num1: int, num2: int):
    await ctx.respond(f"The answer is {num1*num2}!")

@math.command(name = "divide", description = "Divides two numbers together")
async def mathdiv(ctx, numerator: int, denominator: int):
    try:
        await ctx.respond(f"The answer is {numerator/denominator}!")
    except ZeroDivisionError:
        await ctx.respond("Sorry, you can't divide by 0.")
        
bot.add_application_command(math)


@bot.slash_command(name = "songoftheday", description = "Posts today's Song Of The Day")
async def hello(ctx):
    await ctx.respond(song_of_the_day.pick_from_songlist())

bot.run(os.getenv("BOT_TOKEN"))
