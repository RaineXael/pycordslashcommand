
from randomanimal import RandomAnimal
from mathops import do_math
from songoftheday import SongOfTheDay
from fortniteapi import Fortnite
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


# import features for the bot
song_of_the_day = SongOfTheDay()
random_animal = RandomAnimal()
fortnite = Fortnite()


@bot.event
async def on_ready():
    logger.info(f"{bot.user} is ready and online!")


@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!", ephemeral=True)


@bot.slash_command(name="math", description="Do various math operations on two numbers, including decimals")
async def mathadd(ctx, num1: float, operation: str, num2: float):
    await ctx.respond(do_math(num1, operation, num2))


@bot.slash_command(name="songoftheday", description="Posts today's Song Of The Day")
async def hello(ctx):
    try:
        await ctx.respond(song_of_the_day.pick_from_songlist())
    except Exception as e:
        logger.error("Song Of The Day picking error: " + str(e))


@bot.slash_command(name="randomanimal", description="Posts a random specified animal")
async def randomanimal(ctx, animal=None):
    message = random_animal.get_random_animal(animal)
    await ctx.respond(message, ephemeral=random_animal.ephemeral)
    
fn = discord.SlashCommandGroup("fortnite", "Fortnite related commands")

@fn.command(name = "map", description =  "Displays an image of the current map")
async def fn_map(ctx):
    await ctx.respond("Under construction!") 
    
@fn.command(name = "map", description =  "Displays an image of the current map")
async def fn_cosmetic(ctx, skin: str):
    embed = await fortnite.get_character(skin)
    await ctx.respond(embed = embed) 

bot.add_application_command(fn)

bot.run(os.getenv("BOT_TOKEN"))
