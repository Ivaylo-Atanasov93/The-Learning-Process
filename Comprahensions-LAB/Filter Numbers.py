start = int(input())
end = int(input())
filtered_numbers = []
[filtered_numbers.append(num) for num in range(start, end + 1) if any([num % i == 0 for i in range(2, 11)])]
print(filtered_numbers)