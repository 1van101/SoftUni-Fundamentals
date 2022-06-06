import math

name = input()
lenght_of_episode = int(input())
lenght_of_break = int(input())
time_for_lunch = lenght_of_break * 1/8
time_for_rest = lenght_of_break * 1/4
difference = abs(lenght_of_break - (time_for_rest+time_for_lunch+lenght_of_episode))
if lenght_of_episode <= lenght_of_break - (time_for_lunch + time_for_rest):
    print(f"You have enough time to watch {name} and left with {math.ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(difference)} more minutes.")