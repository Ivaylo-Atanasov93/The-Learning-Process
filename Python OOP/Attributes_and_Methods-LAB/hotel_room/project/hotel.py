class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return Hotel(f"{stars_count} stars Hotel")

    def add_room(self, room):
        room_numbers = [room.number for room in self.rooms]
        if room.number not in room_numbers:
            self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = [room for room in self.rooms if room_number == room.number]
        if len(room) != 0 and room[0].capacity >= people and not room[0].is_taken:
            self.guests += people
            return room[0].take_room(people)

    def free_room(self, room_number: int):
        room = [room for room in self.rooms if room_number == room.number]
        if len(room) != 0 and room[0].is_taken:
            self.guests -= room[0].guests
            return room[0].free_room()

    def print_status(self):
        taken_rooms = ", ".join(str(room.number) for room in self.rooms if room.is_taken)
        free_rooms = ", ".join(str(room.number) for room in self.rooms if not room.is_taken)

        print(f'Hotel {self.name} has {self.guests} total guests')
        if free_rooms:
            print(f'Free rooms: {free_rooms}')
        if taken_rooms:
            print(f'Taken rooms: {taken_rooms}')