
import discord
import aiohttp
##-FORTNITE API USED: https://fortnite-api.com/-##

class Fortnite():
    
    
    def __rarity_to_color__(self, color_str="common"):
        #tfs the rarity of a char to a discord color
        if color_str=="legendary":
            color=0xd06f33
        elif color_str=="epic":
            color=0x9539c6
        elif color_str=="rare":
            color=0x0188d4
        elif color_str=="uncommon":
            color=0x44a001
        elif color_str=="marvel":
            color=0xae1e1b
        elif color_str=="dc":
            color=0x1b509c
        elif color_str=="icon":
            color=0x38e5e9
        elif color_str=="frozen":
            color=0xbdd9ef
        elif color_str=="lava":
            color=0x980904
        elif color_str=="dark":
            color=0xc53ba0
        elif color_str=="gaminglegends":
            color=0x381e65
        elif color_str=="starwars":
            color=0x03205e
        elif color_str=="slurp":
            color=0x2688c7
        else:
            #common
            color=0x8e989c
        return color
                
    def __skin_to_embed__(self,json):      
        embed_color = self.__rarity_to_color__(json.get('rarity').get('value'))
        embed = discord.Embed(title=f"{json.get('name')}", description=f"{json.get('description')}", color=embed_color)
        thumbnail_url = json.get('images').get('smallIcon')
        embed.add_field(name="Info", value=f"{json.get('introduction').get('text')}\n{json.get('set').get('text')}")
        embed.set_thumbnail(url=thumbnail_url)
        return embed
        
        
    async def get_character(self, skin_name):
        #returns a discord embed with the specified characted, if found.
        async with aiohttp.ClientSession() as session:
            print(f'https://fortnite-api.com/v2/cosmetics/br/search?name={skin_name}')
            async with session.get(f'https://fortnite-api.com/v2/cosmetics/br/search?name={skin_name}') as r:
                if r.status == 200:
                    js = await r.json()                    
                    return self.__skin_to_embed__(js.get('data'))
                else:
                    print("no lol")
                    return discord.Embed(title="Skin Not Found!", description="Please enter a valid skin name.", color=discord.Color.dark_grey())
        
