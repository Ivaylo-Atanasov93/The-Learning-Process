from Need_For_Speed.project.car import Car


class SportCar(Car):

    def __init__(self, fuel, horse_power):
        Car.DEFAULT_FUEL_CONSUMPTION = 10.0
        super().__init__(fuel, horse_power)
        self.fuel_consumption = Car.DEFAULT_FUEL_CONSUMPTION
