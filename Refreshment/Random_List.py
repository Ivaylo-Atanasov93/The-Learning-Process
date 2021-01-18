import random


class RandomList(list):
    def get_random_element(self):
        number = random.choice(self)
        self.remove(number)
        return number