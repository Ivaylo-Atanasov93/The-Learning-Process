from Zoo.project.mammal import Mammal


class Bear(Mammal):

    def __init__(self, name):
        super().__init__(name)

bear = Bear('Meca')
print(bear.name)
