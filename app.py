import discord
import dotenv
import os
dotenv.load_dotenv()


bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

bot.run(os.getenv("BOT_TOKEN"))