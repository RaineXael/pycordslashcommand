import random
from datetime import datetime


class SOTDSong():
    def __init__(self, title, author, link):
        self.title = title
        self.author = author
        self.link = link

    def __str__(self):

        artist_str = ""
        if len(self.author) > 0:
            artist_str = f" by **{self.author}**"
        return f"The song for {datetime.today().strftime('%Y-%m-%d')} is: **{self.title}**{artist_str}.\n{self.link}"

    def __repr__(self):
        return f"{self.title}-{self.author}-{self.link}"


class SongOfTheDay():

    def pick_from_songlist(self):
        # picks a random song seeded from the current day
        try:
            today = datetime.today().strftime('%Y%m%d')
            random.seed(today)
            random_song_index = random.randint(0, len(self.song_list))
            return self.song_list[random_song_index]
        except Exception as e:
            print(e)
            return f"Sorry, I was unable to get today's song. ({e})"

    def __init__(self):
        # import songlist and keep it in memory
        self.song_list = []

        f = open("songlist.csv", "r", encoding="utf-8")
        for song_str in f.readlines():
            split_str = song_str.split("|")
            song_obj = SOTDSong(split_str[0], split_str[1], split_str[2])
            self.song_list.append(song_obj)
 

