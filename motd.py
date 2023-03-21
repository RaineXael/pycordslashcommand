from discord.ext import tasks, commands
from random import random

class Motd(commands.cog):

    def __init__(self, bot):
        self.bot = bot
        #call change presence at the start if it doesn't already change the presence
        self.change_presence.start()

        self.presences = [
            discord.Activity(type=discord.ActivityType.watching,name='the dev fumble with python'),
            discord.Game(name="Bubsy 3D"),
            discord.Activity(type=discord.ActivityType.listening, name="to the same song on repeat"),
            discord.Streaming(name="to an audience of 0", url="https://www.google.com")
        ]

    def cog_unload(self):
        self.change_presence.cancel()

    @tasks.loop(hours=3)
    async def change_presence(self):
        presenceIndex = randint(0,len(self.presences))
        await bot.change_presence(activity=self.presences[presenceIndex])
            
# Setting `Playing ` status
#await bot.change_presence(activity=discord.Game(name="a game"))

# Setting `Streaming ` status
#await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# Setting `Listening ` status
#await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# Setting `Watching ` status
#await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))
        