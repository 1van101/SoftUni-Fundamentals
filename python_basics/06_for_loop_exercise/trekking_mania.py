number_of_groups = int(input())
total_people = 0
musala_climbers = 0
mont_blant_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0

for i in range(1, number_of_groups + 1):
    number_of_people_in_group = int(input())
    total_people += number_of_people_in_group
    if number_of_people_in_group <= 5:
        musala_climbers += number_of_people_in_group
    elif number_of_people_in_group <= 12:
        mont_blant_climbers += number_of_people_in_group
    elif number_of_people_in_group <= 25:
        kilimanjaro_climbers += number_of_people_in_group
    elif number_of_people_in_group <= 40:
        k2_climbers += number_of_people_in_group
    else:
        everest_climbers += number_of_people_in_group

musala_climbers_percent = musala_climbers / total_people * 100
mont_blant_climbers_percent = mont_blant_climbers / total_people * 100
kilimanjaro_climbers_percent = kilimanjaro_climbers / total_people * 100
k2_climbers_percent = k2_climbers / total_people * 100
everest_climbers_percent = everest_climbers / total_people * 100

print(f"{musala_climbers_percent:.2f}%")
print(f"{mont_blant_climbers_percent:.2f}%")
print(f"{kilimanjaro_climbers_percent:.2f}%")
print(f"{k2_climbers_percent:.2f}%")
print(f"{everest_climbers_percent:.2f}%")


