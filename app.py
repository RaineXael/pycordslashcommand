import discord
import dotenv
import os
import requests
dotenv.load_dotenv()


bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

math = discord.SlashCommandGroup("math", "Math related commands")

@math.command(name = "add", description =  "Add two numbers together")
async def mathadd(ctx, num1: int, num2: int):
    await ctx.respond(f"The answer is {num1+num2}!")

@math.command(name = "subtract", description = "Subtract two numbers together")
async def mathsub(ctx, num1: int, num2: int):
    await ctx.respond(f"The answer is {num1-num2}")

bot.add_application_command(math)

bot.run(os.getenv("BOT_TOKEN"))
