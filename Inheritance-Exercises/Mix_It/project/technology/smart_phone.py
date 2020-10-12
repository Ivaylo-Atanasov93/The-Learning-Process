from Mix_It.project.technology.technology import Technology


class SmartPhone(Technology):

    def __init__(self, memory, memory_taken):
        super().__init__(memory, memory_taken)

    def install_app(self, app, app_memory):
        capacity = self.get_capacity(self.memory, self.memory_taken + app_memory)
        if isinstance(capacity, int or float):
            self.memory_taken += app_memory
            return capacity
        return f"You don't have enough space for {app}!"
