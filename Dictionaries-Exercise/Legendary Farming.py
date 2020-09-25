from collections import defaultdict


def print_dict(dictionary, template):
    for k, v in dictionary.items():
        print(template.format(k, v))


winner_collection = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
collector = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_collector = defaultdict(int)
winner = ''

while winner == '':
    line = input().lower().split()
    for i in range(0, len(line), 2):
        quantity = int(line[i])
        item = line[i + 1]
        if item in collector:
            collector[item] += quantity
            if collector[item] >= 250:
                collector[item] -= 250
                winner += item
                break
        else:
            junk_collector[item] += quantity

sorted_collector = dict(sorted(collector.items(), key=lambda a: (-a[1], a[0])))
sorted_junk_collector = dict(sorted(junk_collector.items()))

print(f'{winner_collection[winner]} obtained!')
print_dict(sorted_collector, "{}: {}")
print_dict(sorted_junk_collector, "{}: {}")
