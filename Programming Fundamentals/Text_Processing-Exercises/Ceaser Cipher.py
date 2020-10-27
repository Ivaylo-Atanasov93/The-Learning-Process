password = input()
ciphered_password = ''

for char in password:
    ciphered_password += chr(ord(char) + 3)

print(ciphered_password)