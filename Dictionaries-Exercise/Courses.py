from collections import defaultdict

courses = defaultdict(list)

end = False

while not end:
    line = input().split(' : ')
    if line[0] == 'end':
        end = True
        break
    module = line[0]
    person = line[1]
    courses[module].append(person)

sorted_courses = dict(sorted(courses.items(), key=lambda x: -len(x[1])))
sorted_courses = {x: sorted(sorted_courses[x]) for x in sorted_courses.keys()}
for key in sorted_courses:
    print(f'{key}: {len(sorted_courses[key])}')
    for person in sorted_courses[key]:
        print(f'-- {person}')
