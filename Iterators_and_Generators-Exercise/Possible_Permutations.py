import itertools

def possible_permutations(iter):
    result = list(itertools.permutations(iter))
    result = [list(item) for item in result]
    yield result


[print(n) for n in possible_permutations([1, 2, 3])]
