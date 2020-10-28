from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        raise NotImplementedError

    @abstractmethod
    def create_sofa(self):
        raise NotImplementedError

    @abstractmethod
    def create_table(self):
        raise NotImplementedError


class Chair:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Sofa:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Table:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class VictorianFactory(AbstractFactory):
    def create_chair(self):
        return Chair('Victorian chair')

    def create_sofa(self):
        return Sofa('Victorian sofa')

    def create_table(self):
        return Table('Victorian table')


class ModernFactory(AbstractFactory):
    def create_chair(self):
        return Chair('Modern chair')

    def create_sofa(self):
        return Sofa('Modern sofa')

    def create_table(self):
        return Table('Modern table')


class FuturisticFactory(AbstractFactory):
    def create_chair(self):
        return Chair('Futuristic chair')

    def create_sofa(self):
        return Sofa('Futuristic sofa')

    def create_table(self):
        return Table('Futuristic chair')


x = FuturisticFactory()
print(x.create_chair())
print(x.create_sofa())
print(x.create_table())
