snowballs_number = int(input())
snowball_value = 0
snowball_weight = 0
snowball_time = 0
snowball_quality = 0
for snowball in range(snowballs_number):
    weight = int(input())
    time_to_reach_the_targer = int(input())
    quality = int(input())
    value = (weight / time_to_reach_the_targer) ** quality
    if value > snowball_value:
        snowball_value = value
        snowball_weight = weight
        snowball_time = time_to_reach_the_targer
        snowball_quality = quality
print(f"{snowball_weight} : {snowball_time} = {int(snowball_value)} ({snowball_quality})")
