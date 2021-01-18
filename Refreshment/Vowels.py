class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels = ['a', 'e', 'i', 'u', 'y', 'o']
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self.string):
            raise StopIteration
        current_letter = self.string[self.counter]
        self.counter += 1

        if current_letter.lower() in self.vowels:
            return current_letter
        return self.__next__()

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
