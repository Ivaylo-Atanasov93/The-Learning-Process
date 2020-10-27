from Need_For_Speed.project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):

    def __init__(self, fuel, horse_power):
        Motorcycle.DEFAULT_FUEL_CONSUMPTION = 8.0
        super().__init__(fuel, horse_power)
        self.fuel_consumption = Motorcycle.DEFAULT_FUEL_CONSUMPTION
