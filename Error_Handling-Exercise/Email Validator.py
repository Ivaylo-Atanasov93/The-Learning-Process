class MustContainAtSymbolError(Exception):
    pass

class NameTooShortError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

domains = ['com', 'bg', 'org', 'net']

while True:
    email = input()
    if email != 'End':
        if '@' not in email:
            raise MustContainAtSymbolError('Email must contain @!')
        name = email.split('@')[0]
        if len(name) <= 4:
            raise NameTooShortError('Name must be more than 4 characters')
        domain = email.split('.')[1]
        if domain not in domains:
            raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
        print('Email is valid')