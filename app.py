from songoftheday import SongOfTheDay
from randomanimal import RandomAnimal
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


math = discord.SlashCommandGroup("math", "Math related commands")


@math.command(name="add", description="Add two numbers together")
async def mathadd(ctx, num1: int, num2: int):
    await ctx.respond(f"The answer is {num1+num2}!")


@math.command(name="subtract", description="Subtract two numbers together")
async def mathsub(ctx, num1: int, num2: int):
    await ctx.respond(f"The answer is {num1-num2}!")


@math.command(name="multiply", description="Multiply two numbers together")
async def mathmult(ctx, num1: int, num2: int):
    await ctx.respond(f"The answer is {num1*num2}!")


@math.command(name="divide", description="Divides two numbers together")
async def mathdiv(ctx, numerator: int, denominator: int):
    try:
        await ctx.respond(f"The answer is {numerator/denominator}!")
    except ZeroDivisionError:
        await ctx.respond("Sorry, you can't divide by 0.")

bot.add_application_command(math)


@bot.slash_command(name="songoftheday", description="Posts today's Song Of The Day")
async def sotd_command(ctx):
    await ctx.respond(song_of_the_day.pick_from_songlist())


@bot.slash_command(name="randomanimal", description="Posts a random specified animal")
async def randomanimal(ctx, animal: str):
    message = random_animal.get_random_animal(animal)
    await ctx.respond(message, ephemeral=random_animal.ephemeral)

bot.run(os.getenv("BOT_TOKEN"))
