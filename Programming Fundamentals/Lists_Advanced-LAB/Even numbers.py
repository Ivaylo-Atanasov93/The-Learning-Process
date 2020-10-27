string = input().split(', ')
even_elements_indexes = [i for i in range(len(string)) if int(string[i]) % 2 == 0]
print(even_elements_indexes)