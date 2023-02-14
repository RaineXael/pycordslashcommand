
from randomanimal import RandomAnimal
from mathops import do_math
from songoftheday import SongOfTheDay
from fortniteapi import Fortnite
from randomcommand import RandomNumbers
from reminder import Reminder
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


# init logger
logger = logging.getLogger('discord')
if is_debug:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.WARN)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


# import features for the bot
song_of_the_day = SongOfTheDay()
random_animal = RandomAnimal()
fortnite = Fortnite(os.getenv("FORTNITE_API_TOKEN"), logger)
reminder = Reminder('./reminder.db',bot)
randomnum = RandomNumbers()

print(os.getenv("FORTNITE_API_TOKEN"))
print(os.getenv("BOT_TOKEN"))

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name='the developper fumble with python'))

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!", ephemeral=True)


@bot.slash_command(name="math", description="Do various math operations on two numbers, including decimals")
async def mathadd(ctx, num1: float, operation: str, num2: float):
    await ctx.respond(do_math(num1, operation, num2))


@bot.slash_command(name="songoftheday", description="Posts today's Song Of The Day")
async def songoftheday(ctx):
    try:
        await ctx.respond(song_of_the_day.pick_from_songlist())
    except Exception as e:
        logger.error("Song Of The Day picking error: " + str(e))


@bot.slash_command(name="randomanimal", description="Posts a random specified animal")
async def randomanimal(ctx, animal=None):
    message = await random_animal.get_random_animal(animal)
    await ctx.respond(message, ephemeral=random_animal.ephemeral)

if os.getenv("FORTNITE_API_TOKEN") != None:

    fn = discord.SlashCommandGroup("fortnite", "Fortnite related commands")

    @fn.command(name="map", description="Displays an image of the current map")
    async def fn_map(ctx):
        embed = await fortnite.get_map()
        await ctx.respond(embed=embed)


    @fn.command(name="cosmetic", description="Search info for a cosmetic by name")
    async def fn_cosmetic(ctx, name: str):
        embed = await fortnite.get_character(name)
        await ctx.respond(embed=embed)


    @fn.command(name="stats", description="Get your fortnite stats")
    async def fn_cosmetic(ctx, user_name: str):
        embed = await fortnite.get_user_data(user_name)
        await ctx.respond(embed=embed)

    bot.add_application_command(fn)
else:
    print("Fortnite API key wasn't found! Skipping the creation of those commands")

rem = discord.SlashCommandGroup("reminder", "Reminder related commands")

@rem.command(name="add", description="Set a reminder for yourself")
async def randomanimal(ctx, message:str, year:str, month:str,day:str,hour:str,minute:str):
    val = await reminder.on_add_reminder(ctx.author.id, message,year,month,day,hour,minute)
    await ctx.respond(val,ephemeral=True)

@rem.command(name="check", description="Check all your active reminders")
async def randomanimal(ctx):
    message = await reminder.get_all_reminders(ctx.author.id)
    #await ctx.respond('Under construction!')
    await ctx.respond(message, ephemeral=True)

#@rem.command(name="toggle24h", description="Toggles the hour entry to 24h time and 12h time")
#async def toggle24h(ctx):
#    await ctx.respond("Under construction!")

bot.add_application_command(rem)

rng = discord.SlashCommandGroup("random", 'Roll a random number')

@rng.command(name='coin', description='Flips a coin')
async def coin_flip(ctx):
    embed = await randomnum.coin_flip()
    await ctx.respond(embed=embed)

@rng.command(name='d6', description='Rolls a 6 sided die')
async def coin_flip(ctx):
    embed = await randomnum.d6_die()
    await ctx.respond(embed=embed)
    
@rng.command(name='custom', description='Selects a number from 0 to the given number')
async def coin_flip(ctx, maximum:int):
    try:
        embed = await randomnum.choice_chance(maximum)
        await ctx.respond(embed=embed)
    except ValueError as e:
        await ctx.respond("Please enter a number above 0.", ephemeral=True)
        

bot.add_application_command(rng)

bot.run(os.getenv("BOT_TOKEN"))
