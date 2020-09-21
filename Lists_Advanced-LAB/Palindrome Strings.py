string = input().split()
palindrome_list = [element for element in string if element == element [::-1]]
searched_palindrome = input()
print(palindrome_list)
print(f'Found palindrome {palindrome_list.count(searched_palindrome)} times')