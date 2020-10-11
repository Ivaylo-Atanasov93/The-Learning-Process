from Wild_Cat_Zoo.project.caretaker import Caretaker
from Wild_Cat_Zoo.project.cheetah import Cheetah
from Wild_Cat_Zoo.project.keeper import Keeper
from Wild_Cat_Zoo.project.lion import Lion
from Wild_Cat_Zoo.project.tiger import Tiger
from Wild_Cat_Zoo.project.vet import Vet


class Zoo:

    def __init__(self, name: str, budget: int, animal_cap: int, workers_cap: int):
        self.__budget = budget
        self.__animal_capacity = animal_cap
        self.__workers_capacity = workers_cap
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif price > self.__budget and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = [worker for worker in self.workers if worker.name == worker_name]
        if len(worker) > 0:
            self.workers.remove(worker[0])
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_of_salaries = sum([worker.salary for worker in self.workers])
        if sum_of_salaries <= self.__budget:
            self.__budget -= sum_of_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_animal_needs = sum([animal.get_needs() for animal in self.animals])
        if sum_animal_needs <= self.__budget:
            self.__budget -= sum_animal_needs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [animal for animal in self.animals if type(animal).__name__ == 'Lion']
        tigers = [animal for animal in self.animals if type(animal).__name__ == 'Tiger']
        cheetahs = [animal for animal in self.animals if type(animal).__name__ == 'Cheetah']
        result = f'You have {len(self.animals)} animals\n'
        result += f'----- {len(lions)} Lions:\n'
        result += "\n".join([repr(lion) for lion in lions])
        result += f'\n----- {len(tigers)} Tigers:\n'
        result += "\n".join([repr(tiger) for tiger in tigers])
        result += f'\n----- {len(cheetahs)} Cheetahs:\n'
        result += "\n".join([repr(cheetah) for cheetah in cheetahs])
        return result

    def workers_status(self):
        keepers = [worker for worker in self.workers if type(worker).__name__ == 'Keeper']
        caretakers = [worker for worker in self.workers if type(worker).__name__ == 'Caretaker']
        vets = [worker for worker in self.workers if type(worker).__name__ == 'Vet']
        result = f'You have {len(self.workers)} workers\n'
        result += f'----- {len(keepers)} Keepers:\n'
        result += "\n".join([repr(keeper) for keeper in keepers])
        result += f'\n----- {len(caretakers)} Caretakers:\n'
        result += "\n".join([repr(caretaker) for caretaker in caretakers])
        result += f'\n----- {len(vets)} Vets:\n'
        result += "\n".join([repr(vet) for vet in vets])
        return result

zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("George"))
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
