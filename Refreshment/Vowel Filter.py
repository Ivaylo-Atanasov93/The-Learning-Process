def vowel_filter(function):
    def wrapper():
        result = []
        func = function()
        vowels = ['a', 'e', 'i', 'u', 'y', 'o']
        for letter in func:
            if letter in vowels:
                result.append(letter)
        return result
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
