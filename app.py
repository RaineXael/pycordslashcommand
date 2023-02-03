
from randomanimal import RandomAnimal
from mathops import do_math
from songoftheday import SongOfTheDay
import discord
import dotenv
import os
# import requests

dotenv.load_dotenv()
bot = discord.Bot()

# import features for the bot
song_of_the_day = SongOfTheDay()
random_animal = RandomAnimal()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!", ephemeral=True)


@bot.slash_command(name="math", description="Do various math operations on two numbers, including decimals")
async def mathadd(ctx, num1: float, operation: str, num2: float):
    await ctx.respond(do_math(num1, operation, num2))


@bot.slash_command(name="songoftheday", description="Posts today's Song Of The Day")
async def hello(ctx):
    await ctx.respond(song_of_the_day.pick_from_songlist())


@bot.slash_command(name="randomanimal", description="Posts a random specified animal")
async def randomanimal(ctx, animal=None):
    message = random_animal.get_random_animal(animal)
    await ctx.respond(message, ephemeral=random_animal.ephemeral)

bot.run(os.getenv("BOT_TOKEN"))
