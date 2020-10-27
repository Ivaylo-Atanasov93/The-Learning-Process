import unittest
from Code_for_Testing.Car_Manager import Car


class TestCarManager(unittest.TestCase):
    def test_CarInit_whenProperInputIsGiven_shouldBeAllRight(self):
        make = 'Mercedes'
        model = "GT"
        fuel_consumption = 20
        capacity = 80
        car = Car(make, model, fuel_consumption, capacity)
        self.assertEqual(make, car.make)
        self.assertEqual(model, car.model)
        self.assertEqual(fuel_consumption, car.fuel_consumption)
        self.assertEqual(capacity, car.fuel_capacity)

    def test_CarInit_whenInvalidMake_shouldRaiseException(self):
        make = None
        model = "GT"
        fuel_consumption = 20
        capacity = 80
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, capacity)
        self.assertIsNotNone(context.exception)

    def test_CarInit_whenEmptyString_shouldRaiseException(self):
        make = ""
        model = "GT"
        fuel_consumption = 20
        capacity = 80
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, capacity)
        self.assertIsNotNone(context.exception)

    def test_CarInit_whenInvalidModel_shouldRaiseException(self):
        make = "Mercedes"
        model = ""
        fuel_consumption = 20
        capacity = 80
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, capacity)
        self.assertIsNotNone(context.exception)

    def test_CarInit_whenNoneModel_shouldRaiseException(self):
        make = "Mercedes"
        model = None
        fuel_consumption = 20
        capacity = 80
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, capacity)
        self.assertIsNotNone(context.exception)

    def test_CarInit_whenNegativeConsumption_shouldRaiseException(self):
        make = "Mercedes"
        model = "GT"
        fuel_consumption = -20
        capacity = 80
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, capacity)
        self.assertIsNotNone(context.exception)

    def test_CarInit_whenZeroConsumption_shouldRaiseException(self):
        make = "Mercedes"
        model = "GT"
        fuel_consumption = 0
        capacity = 80
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, capacity)
        self.assertIsNotNone(context.exception)

    def test_CarInit_whenNegativeCapacity_shouldRaiseException(self):
        make = "Mercedes"
        model = "GT"
        fuel_consumption = 20
        capacity = -80
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, capacity)
        self.assertIsNotNone(context.exception)

    def test_CarInit_whenZeroCapacity_shouldRaiseException(self):
        make = "Mercedes"
        model = "GT"
        fuel_consumption = 20
        capacity = 0
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, capacity)
        self.assertIsNotNone(context.exception)

    def test_CarInit_whenNegativeFuelAmount_shouldRaiseException(self):
        make = "Mercedes"
        model = "GT"
        fuel_consumption = 20
        capacity = 80
        car = Car(make, model, fuel_consumption, capacity)
        with self.assertRaises(Exception) as context:
            car.fuel_amount = -10
        self.assertIsNotNone(context.exception)

    def test_CarRefuel_whenNegativeFuel_shouldRaiseException(self):
        make = "Mercedes"
        model = "GT"
        fuel_consumption = 20
        capacity = 80
        car = Car(make, model, fuel_consumption, capacity)
        with self.assertRaises(Exception) as context:
            car.refuel(-10)
        self.assertIsNotNone(context.exception)

    def test_CarRefuel_whenZeroFuel_shouldRaiseException(self):
        make = "Mercedes"
        model = "GT"
        fuel_consumption = 20
        capacity = 80
        car = Car(make, model, fuel_consumption, capacity)
        with self.assertRaises(Exception) as context:
            car.refuel(0)
        self.assertIsNotNone(context.exception)

    def test_CarRefuel_whenPositiveFuelAndEnoughCapacity_shouldIncreaseFuel(self):
        make = 'Mercedes'
        model = "GT"
        fuel_consumption = 20
        capacity = 80
        refuel_amount = 30
        car = Car(make, model, fuel_consumption, capacity)
        car.refuel(refuel_amount)
        self.assertEqual(refuel_amount, car.fuel_amount)

    def test_CarRefuel_whenPositiveFuelAndMoreThanCapacity_shouldSetAmountToCapacity(self):
        make = 'Mercedes'
        model = "GT"
        fuel_consumption = 20
        capacity = 80
        refuel_amount = 100
        car = Car(make, model, fuel_consumption, capacity)
        car.refuel(refuel_amount)
        self.assertEqual(capacity, car.fuel_capacity)

    def test_CarDrive_whenNotEnoughFuel_shouldRaiseException(self):
        make = 'Mercedes'
        model = "GT"
        fuel_consumption = 20
        capacity = 80
        car = Car(make, model, fuel_consumption, capacity)
        with self.assertRaises(Exception) as context:
            car.drive(1000)
        self.assertIsNotNone(context.exception)

    def test_CarDrive_whenEnoughFuel_shouldDecreaseFuel(self):
        make = 'Mercedes'
        model = "GT"
        fuel_consumption = 20
        capacity = 80
        refuel_amount = 80
        kilometers = 100
        amount_needed = kilometers * fuel_consumption / 100
        car = Car(make, model, fuel_consumption, capacity)
        car.refuel(refuel_amount)
        car.drive(kilometers)
        self.assertEqual(capacity - amount_needed, car.fuel_amount)


if __name__ == "__main__":
    unittest.main()
