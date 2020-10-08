class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if song in self.songs:
            return "Song is already in the album."
        if self.published:
            return "Cannot add songs. Album is published."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."


    def remove_song(self, song_name: str):
        song_for_removing = [s for s in self.songs if song_name == s.name]
        if self.published:
            return "Cannot remove songs. Album is published."
        if len(song_for_removing) == 0:
            return "Song is not in the album."
        self.songs.remove(song_for_removing[0])
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        details = f'Album {self.name}\n'
        for s in self.songs:
            details += f'== {s.get_info()}\n'
        return details
