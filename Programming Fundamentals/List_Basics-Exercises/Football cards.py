team_a = []
team_b = []
red_cards = input().split()
terminated = False
for i in range(1, 12):
    team_a.append(i)
    team_b.append(i)

for j in red_cards:
    team = j[0]
    num = int(j[2:])
    if team == 'A':
        if num not in team_a:
            continue
        else:
            team_a.remove(num)
            if len(team_a) < 7:
                terminated = True
                break
    elif team == 'B':
        if num not in team_b:
            continue
        else:
            team_b.remove(num)
            if len(team_b) < 7:
                terminated = True
                break


if terminated:
    print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
    print('Game was terminated')

else:
    print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')