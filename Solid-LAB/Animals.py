class AnimalsSound:

    animals_sound = {'dog':'woof-woof', 'cat':'meow', 'chicken':'chicken sound'}

    @staticmethod
    def make_sound(animal):
        if animal.species.lower() in AnimalsSound.animals_sound.keys():
            return AnimalsSound.animals_sound[animal.species]
        return 'No such animal sound recorded'

class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


def animal_sound(animals: list):
    for animal in animals:
        print(AnimalsSound.make_sound(animal))



animals = [Animal('cat'), Animal('dog'), Animal('chicken'), Animal('snake')]
animal_sound(animals)

#--------------Initial Code---------------
# Problem:
# 2.	Animals
# Refactor the provided code, so you don't need to make any changes in it when you want to add new species to the animals list

# class Animal:
#     def __init__(self, species):
#         self.species = species
#
#     def get_species(self):
#         return self.species
#
#
# def animal_sound(animals: list):
#     for animal in animals:
#         if animal.species == 'cat':
#             print('meow')
#         elif animal.species == 'dog':
#             print('woof-woof')
#
#
# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)