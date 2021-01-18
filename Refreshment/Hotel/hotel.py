class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return Hotel(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [room for room in self.rooms if room_number == room.number][0]
        if not room.is_taken:
            room.take_room(people)
            self.guests += room.guests

    def free_room(self, room_number):
        room = [room for room in self.rooms if room_number == room.number][0]
        self.guests -= room.guests
        room.free_room()

    def print_status(self):
        free_rooms_numbers = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms_numbers = [str(room.number) for room in self.rooms if room.is_taken]
        print(f'Hotel {self.name} has {self.guests} total guests')
        if free_rooms_numbers:
          print(f'Free rooms: {", ".join(free_rooms_numbers)}')
        if taken_rooms_numbers:
          print(f'Taken rooms: {", ".join(taken_rooms_numbers)}')

