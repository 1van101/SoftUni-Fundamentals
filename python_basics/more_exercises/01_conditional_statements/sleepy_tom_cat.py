holidays_num = int(input())
tom_norm_minutes = 30000
working_days = 365 - holidays_num
holidays_num_minutes_to_play = holidays_num * 127
working_days_to_play = working_days * 63
difference = abs(tom_norm_minutes - (holidays_num_minutes_to_play + working_days_to_play))
hours = difference // 60
minutes = difference % 60
if holidays_num_minutes_to_play + working_days_to_play > tom_norm_minutes:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")

