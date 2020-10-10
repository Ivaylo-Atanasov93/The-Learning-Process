class Equipment:

    autoincremented = 1

    def __init__(self, name):
        self.name = name
        self.id = self.autoincremented
        Equipment.autoincremented += 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.autoincremented