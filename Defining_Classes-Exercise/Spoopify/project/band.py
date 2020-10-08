class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        album_for_removing = [album for album in self.albums if album.name == album_name]
        if len(album_for_removing) == 0:
            return f"Album {album_name} is not found."
        if album_for_removing[0].published:
            return "Album has been published. It cannot be removed."
        self.albums.remove(album_for_removing[0])
        return f"Album {album_name} has been removed."

    def details(self):
        details = f'Band {self.name}\n'
        for album in self.albums:
            details += f'{Album.details(album)}\n'
        return details


# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())

'Removed song Scavenger of Human Sorrow from album The Sound of Perseverance'
'Removed song Scavenger of Human Sorrow from album The Sound of Perseverance.'
