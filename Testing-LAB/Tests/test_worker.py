import unittest

from Code_for_Testing.Worker import Worker


class TestWorker(unittest.TestCase):
    #•	Test if the worker is initialized with correct name, salary and energy
    def test_workerInit_whenCorrectNameSalaryAndEnergy_shouldBeInitialized(self):
        name = "Worker name"
        salary = 123
        energy = 5
        worker = Worker(name, salary, energy)
        self.assertEqual(name, worker.name)
        self.assertEqual(salary, worker.salary)
        self.assertEqual(energy, worker.energy)
        self.assertEqual(0, worker.money)

    def test_workerRest_whenRestMethodIsCalled_shouldIncrementEnergy(self):
        #•	Test if the worker's energy is incremented after the rest method is called
        name = "Worker name"
        salary = 123
        energy = 5
        worker = Worker(name, salary, energy)
        worker.rest()
        self.assertEqual(energy + 1, worker.energy)

    def test_workerWork_whenEnergyIsNegativeOrEqualToZero_shouldRaiseException(self):
        #•	Test if an error is raised if the worker tries to work with negative energy or equal to 0
        name = "Worker name"
        salary = 123
        energy = 0
        worker = Worker(name, salary, energy)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertIsNotNone(context.exception)

    def test_workerWorkSalary_whenWorkMeshodIsCalled_shouldIncreaseTheSalary(self):
        #•	Test if the worker's money is increased by his salary correctly after the work method is called
        name = "Worker name"
        salary = 123
        energy = 5
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(salary, worker.money)

    def test_workerWorkEnergy_whenWorkMethodIsCalled_shouldDecreaseTheEnergy(self):
        #•	Test if the worker's energy is decreased after the work method is called
        name = "Worker name"
        salary = 123
        energy = 5
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(energy - 1, worker.energy)

    def test_workerGetInfo_whenGetInfoMethodIsCalled_shouldReturnProperStringAndValues(self):
        #•	Test if the get_info method returns the proper string with correct values
        name = "Worker name"
        salary = 123
        energy = 5
        worker = Worker(name, salary, energy)
        money = worker.money
        info = f'{name} has saved {money} money.'
        result = worker.get_info()
        self.assertEqual(info, result)

if __name__ == "__main__":
    unittest.main()