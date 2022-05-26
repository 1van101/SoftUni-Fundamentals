capacity = 255
liters_counter = 0
number_of_lines = int(input())
for lines in range(number_of_lines):
    liters_of_water = int(input())
    liters_counter += liters_of_water
    if liters_counter > capacity:
        print("Insufficient capacity!")
        liters_counter -= liters_of_water
print(liters_counter)