import requests

## --Hourly Animal API by tinyfox.dev--##


class RandomAnimal():
    def __init__(self):
        r = requests.get('https://api.tinyfox.dev/img?animal=animal&json')
        self.available_anmials = r.json().get('available')
        self.ephemeral = False  # states wether response is ephmeral or not
        print("Random Animal Class Ready")

    def get_random_animal(self, animal):
        if animal is not None:
            for this_animal in self.available_anmials:
                if this_animal == animal:
                    self.ephemeral = False
                    pic_link = requests.get(
                        f"https://api.tinyfox.dev/img?animal={animal}&json").json().get('loc')
                    return f'**{this_animal}**, Hourly Animal API by tinyfox.dev\nhttps://tinyfox.dev{pic_link}'
            self.ephemeral = True
            return f"The animal you entered wasn't found! Please enter one of the following as a parameter:\n{self.available_anmials}"
        self.ephemeral = True
        return f"This command sends a random image of an animal entered of the following list:\n{self.available_anmials}"
