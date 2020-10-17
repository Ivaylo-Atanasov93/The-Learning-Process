def get_primes(iter):
    for num in iter:
        prime = True
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    prime = False
                    break
            if prime:
                yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
