from Mix_It.project.vehicle.vehicle import Vehicle


class Plane(Vehicle):

    def __init__(self, available_seats, rows, seats_per_row):
        super().__init__(available_seats)
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats_available = {}

    def buy_tickets(self, row_number, tickets_count):

        if row_number > self.rows or row_number <= 0:
            return f"There is no row {row_number} in the plane!"

        if row_number not in self.seats_available.keys():
            self.seats_available[row_number] = self.seats_per_row
        message = self.get_capacity(self.seats_available[row_number], tickets_count)

        if isinstance(message, int):
            self.seats_available[row_number] -= tickets_count
            return tickets_count
        return f"Not enough tickets on row {row_number}!"
