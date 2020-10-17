class dictionary_iter:

    def __init__(self, iter):
        self.iter = iter
        self.keys = list(self.iter.keys())
        self.counter = 0
        self.end = len(iter)

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.end:
            raise StopIteration
        key = self.keys[self.counter]
        value = self.iter[key]
        self.counter += 1
        return (key, value)

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
