from Mix_It.project.technology.technology import Technology


class Laptop(Technology):

    def __init__(self, memory, memory_taken):
        super().__init__(memory, memory_taken)

    def install_software(self, software, software_memory):
        capacity = self.get_capacity(self.memory, self.memory_taken + software_memory)
        if isinstance(capacity, int or float):
            self.memory_taken += software_memory
            return capacity
        return f"You don't have enough space for {software}!"
