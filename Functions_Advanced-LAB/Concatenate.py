def concatenate(*args):
    strings = args
    result = ''
    for word in strings:
        result += word
    return result


print(concatenate("Soft", "Uni", "Is", "Great", "!"))