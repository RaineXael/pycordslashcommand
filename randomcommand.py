import random
import discord

class RandomNumbers:

    async def coin_flip(self):
        #make an embed with the result of either 0 or 1 and make it look good
        result = random.randint(0,1)
        if result == 0:
            desc = "Tails"
        else:
            desc = "Heads"
        embed = discord.Embed(title='Coinflip', description=f'The coin landed on {desc}')
        #todo: put an image for its respective result
        return embed
        

    async def d6_die(self):
        #embed for a 6 sided die result
        result = random.randint(1,6)
        embed = discord.Embed(title='D6', description=f'The die landed on {result}')
        #todo: put an image for its respective result
        return embed

    async def choice_chance(self,maximum):
        #do a roll from 0 to maximum and return an embed with the result
        if maximum <= 0:
            raise ValueError
        result = random.randint(0,maximum)
        embed = discord.Embed(title=f'Custom Chance: 0 to {maximum}', description=f'From 0 to {maximum}, {result} was picked.')
        return embed

    
