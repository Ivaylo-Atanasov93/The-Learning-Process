class Vehicle:

    DEFAULT_FUEL_CONSUMPTION = 1.25
    fuel_consumption = float
    fuel = float
    horse_power = int

    def __init__(self, fuel, horse_power):
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        kilometers_available = self.fuel / self.fuel_consumption
        if kilometers_available >= kilometers:
            self.fuel -= kilometers * self.fuel_consumption

