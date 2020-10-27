line = input().split()
revision = {}
for i in range(0, len(line), 2):
    key = line[i]
    value = line[i + 1]
    revision[key] = int(value)

print(revision)
