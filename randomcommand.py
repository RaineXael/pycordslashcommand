import random
import discord


class RandomNumbers:

    def __init__(self) -> None:
        self.dice_images = ['https://i.imgur.com/0dJ6L4e.png', 'https://i.imgur.com/lsveUxw.png', 'https://i.imgur.com/8uCyWsw.png',
                            'https://i.imgur.com/P1o5soc.png', 'https://i.imgur.com/IoGcW3R.png', 'https://i.imgur.com/Ahh7Rpa.png']

    async def coin_flip(self):
        # make an embed with the result of either 0 or 1 and make it look good
        result = random.randint(0, 1)
        url='https://i.imgur.com/KCfYTxz.png'
        if result == 0:
            desc = "Tails"
            url='https://i.imgur.com/MTLz6G7.png'
        else:
            desc = "Heads"
        embed = discord.Embed(
            title='Coinflip', description=f'The coin landed on {desc}')
        embed.set_thumbnail(url=url)
        return embed

    async def d6_die(self):
        # embed for a 6 sided die result

        result = random.randint(1, 6)
        embed = discord.Embed(
            title='D6', description=f'The die landed on {result}')
        url = self.dice_images[result - 1]
        print(url)
        embed.set_thumbnail(url=url)
        return embed

    async def choice_chance(self, maximum):
        # do a roll from 0 to maximum and return an embed with the result
        if maximum <= 0:
            raise ValueError
        result = random.randint(0, maximum)
        embed = discord.Embed(
            title=f'Custom Chance: 0 to {maximum}', description=f'From 0 to {maximum}, {result} was picked.')
        return embed
