class take_skip:
    def __init__(self, step, numbers):
        self.step = step
        self.count = numbers
        self.start = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.count:
            raise StopIteration
        num = self.start
        self.start += self.step
        self.counter += 1
        return num



numbers = take_skip(2, 6)
for number in numbers:
    print(number)

print()

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
