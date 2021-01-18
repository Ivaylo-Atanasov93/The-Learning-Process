class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.num = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 0:
            raise StopIteration
        self.num -= 1
        return self.iterable[self.num]

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
