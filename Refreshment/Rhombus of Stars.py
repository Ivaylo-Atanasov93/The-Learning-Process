class Stars:
    def __init__(self, num):
        self.num = num

    def print_stars(self):
        [print(' ' * (self.num - i) + '* ' * i) for i in range(1, self.num + 1)]
        [print(' ' * (self.num - i) + '* ' * i) for i in range(self.num - 1, 0, -1)]


solve = Stars(int(input()))
solve.print_stars()