class sequence_repeat:

    def __init__(self, text, length):
        self.text = text
        self.lenght = length
        self.counter = 0
        self.letter_counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.lenght:
            raise StopIteration
        current_letter = self.text[self.letter_counter]
        self.counter += 1
        self.letter_counter += 1
        if self.letter_counter == len(self.text):
            self.letter_counter = 0
        return current_letter

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

