from Mix_It.project.capacity_mixin import CapacityMixin



class ParkingMall(CapacityMixin):

    def __init__(self, parking_lots):
        self.parking_lots = parking_lots

    def check_availability(self):
        message = self.get_capacity(self.parking_lots, 1)
        if isinstance(message, int):
            self.parking_lots -= 1
            return f"Parking lots available: {self.parking_lots}"
        else:
            return "There are no more parking lots!"

# park = ParkingMall(3)
# park.check_availability()
# park.check_availability()
# print(park.parking_lots)
# print(park.check_availability())
# print(park.check_availability())