
import discord
import aiohttp
##-FORTNITE API USED: https://fortnite-api.com/-##

class Fortnite():
    async def get_character(self, skin_name):
        #returns a discord embed with the specified characted, if found.
        #check if found first
        #async with aiohttp.ClientSession() as session:
        #    async with session.get(f"https://fortnite-api.com/v2/cosmetics/br/search?name={skin_name}") as r:
        #        if r.status == 200:
        #            #do stuff
        #            print(r.text)
        #            embed = discord.Embed(title="embed Skin Found!", description="description", color=discord.Color.dark_grey())
        #        else:
        #            embed = discord.Embed(title="embed Skin Not Found!", description="description", color=discord.Color.dark_grey())
        #            return embed
        async with aiohttp.ClientSession() as session:
            print(f'https://fortnite-api.com/v2/cosmetics/br/search?name={skin_name}')
            async with session.get(f'https://fortnite-api.com/v2/cosmetics/br/search?name={skin_name}') as r:
                if r.status == 200:
                    js = await r.json()
                    print(js)
                    return discord.Embed(title=f"{skin_name} found", description="description", color=discord.Color.fuchsia())
                else:
                    print("no lol")
                    return discord.Embed(title="embed Skin Not Found!", description="description", color=discord.Color.dark_grey())
                
            
                
        
