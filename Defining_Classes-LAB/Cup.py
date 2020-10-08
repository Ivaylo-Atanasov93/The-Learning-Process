class Cup:
    def __init__(self, size, quantity):
        self.size = int(size)
        self.quantity = int(quantity)

    def fill(self, milliliters):
        if milliliters > self.status():
            return
        self.quantity += milliliters

    def status(self):
        return self.size - self.quantity


class Cup2:
    def __init__(self, size, quantity):
        self.size = int(size)
        self.quantity = int(quantity)

    def can_fill(self, milliliters):
        return milliliters <= self.status()

    def fill(self, add_quantity):
        if self.can_fill(add_quantity):
            self.quantity += add_quantity

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
cup.fill(45)
cup.fill(6)
print(cup.status())

cup = Cup(100, 50)
cup.fill(45)
cup.fill(6)
print(cup.status())
