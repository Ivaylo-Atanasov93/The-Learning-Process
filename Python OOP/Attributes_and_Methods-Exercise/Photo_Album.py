import math


class PhotoAlbum:

    def __init__(self, pages:int):
        self.pages = pages
        self.photos = [[] for i in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label:str):
        free_slot = ''
        for page in range(self.pages):
            if len(self.photos[page]) < 4:
                free_slot = [page, len(self.photos[page])]
                break
        if free_slot == '':
            return "No more free spots"
        page, slot = free_slot
        self.photos[page].append(label)
        return f"{label} photo added successfully on page {page + 1} slot {slot + 1}"

    def display(self):
        return PhotoAlbum.__repr__(self)

    def __repr__(self):
        album = '-' * 11 + '\n'
        for page in self.photos:
            if len(page) > 0:
                album += ('[] ' * len(page)).strip() + '\n'
            else:
                album += '\n'
            album += '-' * 11 + '\n'
        # album += '\n'
        return album

album = PhotoAlbum(3)
album2 = PhotoAlbum.from_photos_count(6)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.display())
print(album2.photos)
print(album2.display())