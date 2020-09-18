n = int(input())
negatives = []
positives = []

for _ in range(0, n):
    number = int(input())
    if number >= 0:
        positives.append(number)
    else:
        negatives.append(number)

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}')