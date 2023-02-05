
import discord
import aiohttp
##-FORTNITE API USED: https://fortnite-api.com/-##

class Fortnite():
    
    def __init__(self, api_token, logger):
        self.logger = logger
        self.api_token={'Authorization': api_token}
    
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
            
    def date_simplifier(self,string):
        #makes the date format given by the json into a more friendly looking string
        print(string)
        month = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']
        splitstr = string.split('T')[0].split('-')
        return f'{month[int(splitstr[1])-1]} {splitstr[2]} {splitstr[0]}'
                
    def __get_cosmetic_set__(self,json):
        try:
            return json.get('set').get('text')
        except:
            return "Not a part of a set."
        
    def __get_cosmetic_last_seen__(self,json):
        try:
            dates = json.get('shopHistory')
            return self.date_simplifier(dates[len(dates)-1])
        except:
            return "Not a shop item."
                
    def __skin_to_embed__(self,json):      
        embed_color = self.__rarity_to_color__(json.get('rarity').get('value'))
        embed = discord.Embed(title=f"{json.get('name')}", description=f"{json.get('description')}", color=embed_color)
        thumbnail_url = json.get('images').get('icon')
        embed.add_field(name="Info", value=f"{json.get('introduction').get('text')}\n{self.__get_cosmetic_set__(json)}", inline=False)
        embed.set_image(url=thumbnail_url)
        embed.set_footer(text="Data provided by: fortnite-api.com")
        embed.add_field(name="Date Added", value=self.date_simplifier(json.get('added')),inline=True)    
        embed.add_field(name="Last Seen", value=self.__get_cosmetic_last_seen__(json), inline=True)
        return embed
            
    async def get_character(self, skin_name):
        #returns a discord embed with the specified characted, if found.
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://fortnite-api.com/v2/cosmetics/br/search?name={skin_name}') as r:
                if r.status == 200:
                    js = await r.json()                    
                    return self.__skin_to_embed__(js.get('data'))
                else:
                    return discord.Embed(title="Skin Not Found!", description="Please enter a valid skin name.", color=discord.Color.dark_grey())
    
              
    async def get_map(self):
        #returns a discord embed with the specified characted, if found.
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://fortnite-api.com/v1/map') as r:
                if r.status == 200:
                    js = await r.json()   
                    embed = discord.Embed(title="The Fortnite Map", color=discord.Color.green()) #todo put the current season and week in there
                    embed.set_image(url=js.get('data').get('images').get('pois'))
                    return embed              
                else:
                    return discord.Embed(title="Map could not be found!", description="Please try later.", color=discord.Color.dark_grey())
    
    async def generate_user_embed(self,js):
        battlepass_stats = f"Level {js.get('battlePass').get('level')}, {js.get('battlePass').get('progress')}% to the next level"
        print("image: " + str(js.get('image')))
        embed = discord.Embed(title=js.get('account').get('name'), description=battlepass_stats, color=0xd06f33)    
        embed.set_image(url=js.get('image'))
        return embed
    
    async def get_user_data(self, user_name):
        async with aiohttp.ClientSession() as session:
            print(self.api_token)
            async with session.get(f'https://fortnite-api.com/v2/stats/br/v2?name={user_name}&image=all', headers=self.api_token) as r:
                    
                    if r.status == 200:
                        js = await r.json()
                        print(js.get('data').get('image'))
                        return await self.generate_user_embed(js.get('data'))
                    elif r.status == 400:
                        return discord.Embed(title=f"User \'{user_name}\' not found!", description="Please try again.", color=discord.Color.dark_grey())
                    elif r.status == 403:
                        discord.Embed(title=f"User \'{user_name}\''s stats are private.", color=discord.Color.dark_grey())
                    else:
                        return discord.Embed(title="Data could not be found!", description="Please try later.", color=discord.Color.dark_grey())
        
    
    
        
    
    
