
import discord
import aiohttp
##-FORTNITE API USED: https://fortnite-api.com/-##

class Fortnite():
    async def get_character(self, skin_name):
        #returns a discord embed with the specified characted, if found.
        async with aiohttp.ClientSession() as session:
            print(f'https://fortnite-api.com/v2/cosmetics/br/search?name={skin_name}')
            async with session.get(f'https://fortnite-api.com/v2/cosmetics/br/search?name={skin_name}') as r:
                if r.status == 200:
                    js = await r.json()                    
                    return 
                else:
                    print("no lol")
                    return discord.Embed(title="Skin Not Found!", description="Please enter a valid skin name.", color=discord.Color.dark_grey())
                
    def __skin_to_embed__(json)        
        #temp
        return discord.Embed(title=f"", description="", color=discord.Color.fuchsia())
    
    def __rarity_to_color__()
        #tfs the rarity of a char to a discord color
