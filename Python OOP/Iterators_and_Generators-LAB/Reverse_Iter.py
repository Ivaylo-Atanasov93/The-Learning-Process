class reverse_iter:

    def __init__(self, iter):
        self.iter = iter[::-1]
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == len(self.iter):
            raise StopIteration
        current_element = self.iter[self.counter]
        self.counter += 1
        return current_element


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
