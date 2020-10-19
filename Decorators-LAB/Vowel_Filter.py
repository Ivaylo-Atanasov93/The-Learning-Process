def vowel_filter(function):
    def wrapper():
        vowels = ['a', 'o', 'u', 'e', 'i', 'y']
        result = function()
        result = [letter for letter in result if letter in vowels]
        return result
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
