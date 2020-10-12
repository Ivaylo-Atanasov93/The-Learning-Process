from Need_For_Speed.project.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, fuel, horse_power):
        Vehicle.DEFAULT_FUEL_CONSUMPTION = 3.0
        super().__init__(fuel, horse_power)
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION

