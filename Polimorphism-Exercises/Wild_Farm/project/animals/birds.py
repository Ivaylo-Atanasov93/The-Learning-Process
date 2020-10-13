from Wild_Farm.project.animals.animal import Bird
from Wild_Farm.project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return  "Hoot Hoot"

    def feed(self, food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += 0.25  * food.quantity
        else:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

class Hen(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return  "Cluck"

    def feed(self, food):
            self.food_eaten += food.quantity
            self.weight += 0.35 * food.quantity

# owl = Owl("Pip", 10, 10)
# print(owl)
# meat = Meat(4)
# veg = Vegetable(1)
# fruit = Fruit(5)
# seed = Seed(3)
# print(owl.make_sound())
# print(owl.feed(meat))
# print(owl.feed(veg))
# print(owl.feed(fruit))
# print(owl.feed(seed))
# print(owl)
# print('-----------Expected-----------')
# print('Owl [Pip, 10, 10, 0]')
# print('Hoot Hoot')
# print('None')
# print('Owl does not eat Vegetable!')
# print('Owl does not eat Fruit!')
# print('Owl does not eat Seed!')
# print('Owl [Pip, 10, 11.0, 4]')
# print()
# hen = Hen("Harry", 10, 10)
# print(hen)
# meat = Meat(4)
# veg = Vegetable(1)
# fruit = Fruit(5)
# seed = Seed(3)
# print(hen.make_sound())
# print(hen.feed(meat))
# print(hen.feed(veg))
# print(hen.feed(fruit))
# print(hen.feed(seed))
# print(hen)
# print('-----------Expected-----------')
# print('Hen [Harry, 10, 10, 0]')
# print('Cluck')
# print('None')
# print('None')
# print('None')
# print('None')
# print('Hen [Harry, 10, 14.55, 13]')
# print([x.__name__ for x in Bird.__bases__])
