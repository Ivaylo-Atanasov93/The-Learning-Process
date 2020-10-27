from Mix_It.project.vehicle.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, available_seats:int, fuel_tank:int, fuel_consumption:float, fuel:float):
        super().__init__(available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, fuel):
        if self.fuel_tank < fuel:
            self.__fuel = self.fuel_tank
            return
        self.__fuel = fuel

    def drive(self, distance):
        kilometers_available = self.__fuel / self.fuel_consumption
        if kilometers_available >= distance:
            self.__fuel -= distance * self.fuel_consumption
            return "We've enjoyed the travel!"

    def refuel(self, liters):
        capacity = self.fuel_tank - self.__fuel
        message = self.get_capacity(capacity, liters)
        if isinstance(message, int):
            self.__fuel += liters
            return self.fuel
        return self.fuel


# car = Car(4, 50, 5, 30)
# print(car.refuel(20))
# car.drive(1)
# print(car.refuel(10))