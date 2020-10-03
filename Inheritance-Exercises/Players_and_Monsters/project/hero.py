class Hero:
    def __init__(self, name, level):
        self.__name = name
        self.__level = level

    def __repr__(self):
        return f"{self.__name} of type {type(self).__name__} has level {self.__level}"