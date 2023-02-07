import aiohttp
## --Hourly Animal API by tinyfox.dev--##


class RandomAnimal:
    def __init__(self):
        self.ephemeral = False
        self.available_animals = []

    async def get_available_animals(self):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.tinyfox.dev/img?animal=animal&json') as r:
                self.available_anmials = r.json().get('available')
        
    
    async def get_random_animal(self, animal):
        if animal is not None:
            for this_animal in self.available_anmials:
                if this_animal == animal:
                    self.ephemeral = False
                    async with aiohttp.ClientSession() as session:
                        async with session.get(f"https://api.tinyfox.dev/img?animal={animal}&json") as r:
                            #return f'**{this_animal}**, Hourly Animal API by tinyfox.dev\nhttps://tinyfox.dev{pic_link}'
                            if r.status == 200:
                                js = await r.json
                                return js
                            else:
                                self.ephemeral = True
                                return "Unable to fetch the animal image from the server"
                self.ephemeral = True
                return f"The animal you entered wasn't found! Please enter one of the following as a parameter:\n{self.available_anmials}"
        self.ephemeral = True
        return f"This command sends a random image of an animal entered of the following list:\n{self.available_anmials}"
