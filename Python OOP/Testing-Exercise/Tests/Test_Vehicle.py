import unittest
from Code_For_Testing.Vehicle import Vehicle, Car, Truck


class TestCar(unittest.TestCase):
    def test_initCar_shouldInitializeNewInstance(self):
        fuel = 80
        consumption = 1
        car = Car(fuel, consumption)
        self.assertEqual(fuel, car.fuel_quantity)
        self.assertEqual(consumption, car.fuel_consumption)

    def test_whenDriveMethodIsCalledAndEnoughFuel_shouldDecreaseTheFuel(self):
        fuel = 80
        consumption = 1
        air_conditioner = 0.9
        distance = 40
        car = Car(fuel, consumption)
        car.drive(distance)
        expected = fuel - (distance * (consumption + air_conditioner))
        result = car.fuel_quantity
        self.assertEqual(expected, result)

    def test_whenDriveMethodIsCalledAndNotEnoughFuel_shouldDoNoting(self):
        fuel = 80
        consumption = 1
        distance = 100
        car = Car(fuel, consumption)
        car.drive(distance)
        expected = fuel
        result = car.fuel_quantity
        self.assertEqual(expected, result)

    def test_whenRefuelMethodIsCalled_shouldIncreaseTheFuel(self):
        fuel = 10
        consumption = 1
        amount = 50
        car = Car(fuel, consumption)
        car.refuel(amount)
        expected = fuel + amount
        result = car.fuel_quantity
        self.assertEqual(expected, result)


class TestTruck(unittest.TestCase):
    def test_initTruck_shouldInitializeNewInstance(self):
        fuel = 80
        consumption = 1
        truck = Truck(fuel, consumption)
        self.assertEqual(fuel, truck.fuel_quantity)
        self.assertEqual(consumption, truck.fuel_consumption)

    def test_whenDriveMethodIsCalledAndEnoughFuel_shouldDecreaseTheFuel(self):
        fuel = 80
        consumption = 1
        fuel_loses = 1.6
        distance = 10
        truck = Truck(fuel, consumption)
        truck.drive(distance)
        expected = fuel - (distance * (consumption + fuel_loses))
        result = truck.fuel_quantity
        self.assertEqual(expected, result)

    def test_whenDriveMethodIsCalledAndNotEnoughFuel_shouldDoNoting(self):
        fuel = 80
        consumption = 1
        distance = 100
        truck = Truck(fuel, consumption)
        truck.drive(distance)
        expected = fuel
        result = truck.fuel_quantity
        self.assertEqual(expected, result)

    def test_whenRefuelMethodIsCalled_shouldIncreaseTheFuel(self):
        fuel = 10
        consumption = 1
        amount = 50
        truck = Truck(fuel, consumption)
        truck.refuel(amount)
        expected = fuel + (amount * 0.95)
        result = truck.fuel_quantity
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
