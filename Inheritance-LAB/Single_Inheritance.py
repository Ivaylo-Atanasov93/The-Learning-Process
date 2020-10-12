class Animal:
    def eat(self):
        return 'eating...'

class Dog(Animal):
    def bark(self):
        return 'barking...'

x = Animal()
y = Dog()

print(x.eat())
print(y.eat())
print(y.bark())