import itertools

def possible_permutations(iter):
    for permutation in itertools.permutations(iter):
        yield list(permutation)



[print(n) for n in possible_permutations([1, 2, 3])]
