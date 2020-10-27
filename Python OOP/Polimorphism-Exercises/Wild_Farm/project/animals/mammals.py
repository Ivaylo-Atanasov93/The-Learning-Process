from Wild_Farm.project.animals.animal import Mammal
from Wild_Farm.project.food import Meat, Vegetable, Fruit, Seed


class Mouse(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return  "Squeak"

    def feed(self, food):
        if isinstance(food, Vegetable) or isinstance(food, Fruit):
            self.food_eaten += food.quantity
            self.weight += 0.10  * food.quantity
        else:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"


class Dog(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return  "Woof!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += 0.40  * food.quantity
        else:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

class Cat(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return  "Meow"

    def feed(self, food):
        if isinstance(food, Vegetable) or isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += 0.30  * food.quantity
        else:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

class Tiger(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return  "ROAR!!!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += 1.00  * food.quantity
        else:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"


# mouse = Mouse("Jerry", 10, 10)
# print(mouse)
# meat = Meat(4)
# veg = Vegetable(1)
# fruit = Fruit(5)
# seed = Seed(3)
# print(mouse.make_sound())
# print(mouse.feed(meat))
# print(mouse.feed(veg))
# print(mouse.feed(fruit))
# print(mouse.feed(seed))
# print(mouse)
# print('-----------Expected-----------')
# print('Mouse [Jerry, 10, 10, 0]')
# print('Squeak')
# print('Mouse does not eat Meat!')
# print('None')
# print('None')
# print('Mouse does not eat Seed!')
# print('Mouse [Jerry, 10.6, 10, 6]')
#
# print()
# doggy = Dog("Freddy", 10, 10)
# print(doggy)
# meat = Meat(4)
# veg = Vegetable(1)
# fruit = Fruit(5)
# seed = Seed(3)
# print(doggy.make_sound())
# print(doggy.feed(meat))
# print(doggy.feed(veg))
# print(doggy.feed(fruit))
# print(doggy.feed(seed))
# print(doggy)
# print('-----------Expected-----------')
# print('Dog [Freddy, 10, 10, 0]')
# print('Woof')
# print('None')
# print('Dog does not eat Vegetable!')
# print('Dog does not eat Fruit!')
# print('Dog does not eat Seed!')
# print('Dog [Freddy, 11.6, 10, 4]')
#
# print()
# kitty = Cat("Tom", 10, 10)
# print(kitty)
# meat = Meat(4)
# veg = Vegetable(1)
# fruit = Fruit(5)
# seed = Seed(3)
# print(kitty.make_sound())
# print(kitty.feed(meat))
# print(kitty.feed(veg))
# print(kitty.feed(fruit))
# print(kitty.feed(seed))
# print(kitty)
# print('-----------Expected-----------')
# print('Cat [Tom, 10, 10, 0]')
# print('Meow')
# print('None')
# print('None')
# print('Cat does not eat Fruit!')
# print('Cat does not eat Seed!')
# print('Cat [Tom, 11.5, 10, 5]')
#
# print()
# tyga = Tiger("Tigero", 10, 10)
# print(tyga)
# meat = Meat(4)
# veg = Vegetable(1)
# fruit = Fruit(5)
# seed = Seed(3)
# print(tyga.make_sound())
# print(tyga.feed(meat))
# print(tyga.feed(veg))
# print(tyga.feed(fruit))
# print(tyga.feed(seed))
# print(tyga)
# print('-----------Expected-----------')
# print('Tiger [Tigero, 10, 10, 0]')
# print('ROAR!!!')
# print('None')
# print('Tiger does not eat Vegetable!')
# print('Tiger does not eat Fruit!')
# print('Tiger does not eat Seed!')
# print('Tiger [Tigero, 14.0, 10, 4]')