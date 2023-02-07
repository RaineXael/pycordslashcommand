import aiohttp
## --Hourly Animal API by tinyfox.dev--##


class RandomAnimal:
    def __init__(self):
        self.ephemeral = False

    async def get_random_animal(self, animal):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.tinyfox.dev/img?animal={animal}&json") as r:
                if r.status == 200:
                    js = await r.json()
                    pic_link = js.get('loc')
                    if pic_link != None:
                        return f'**{animal}**, Hourly Animal API by tinyfox.dev\nhttps://tinyfox.dev{pic_link}'
                    available_animals = js.get('available')
                    if available_animals != None:
                        return 'The animal you entered wasn\'t found. Please enter the following:\n' + str(available_animals)
                else:
                    return 'The animal you entered wasn\'t found.'
                    self.ephemeral = True
                    return "Unable to fetch the animal image from the server"
