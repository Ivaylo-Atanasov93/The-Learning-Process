def solution():

    def integers():
        counter = 1
        while True:
            yield counter
            counter += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        my_list = []
        for num in seq:
            if len(my_list) == n:
                return my_list
            my_list.append(num)


    return (take, halves, integers)

take = solution()[0]
halves = solution()[1]
print(list(take(5, halves())))
