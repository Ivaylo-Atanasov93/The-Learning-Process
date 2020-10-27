def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        result[name] = kwargs[name[0]]
    return result


def age_assignment1(*args, **kwargs):
    result = {name: kwargs[name[0]] for name in args}
    return result


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment1("Amy", "Bill", "Willy", W=36, A=22, B=61))
print(age_assignment1("Peter", "George", G=26, P=19))
