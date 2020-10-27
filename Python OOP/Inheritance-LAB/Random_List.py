import random

class RandomList(list):
    def get_random_element(self):
        element = random.choice(self)
        self.remove(element)
        return element

li = RandomList()
li.append(4)
li.append(3)
li.append(5)
print(li.get_random_element(), 5)

li = RandomList()
li.append(6)
li.append(1.3)
li.append(10)
li.pop()
li.reverse()
print(li.get_random_element())