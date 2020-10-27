n = int(input())
best_value = 0
current_ball = 0
best_snowball_snow = 0
best_snowball_time = 0
best_snowball_quality = 0
for i in range(1, n + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    current_ball = (snowball_snow / snowball_time) ** snowball_quality
    if current_ball > best_value:
        best_value = current_ball
        best_snowball_snow = snowball_snow
        best_snowball_quality = snowball_quality
        best_snowball_time = snowball_time

print(f'{best_snowball_snow} : {best_snowball_time} = {int(best_value)} ({best_snowball_quality})')