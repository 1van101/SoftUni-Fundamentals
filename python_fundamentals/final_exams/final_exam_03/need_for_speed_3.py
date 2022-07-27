def drive_the_car(dct, info):
    car = info[1]
    distance = int(info[2])
    fuel = int(info[3])
    if dct[car]["fuel"] < fuel:
        print("Not enough fuel to make that ride")
    else:
        dct[car]["fuel"] -= fuel
        dct[car]["mileage"] += distance
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if dct[car]["mileage"] >= 100_000:
            print(f"Time to sell the {car}!")
            del dct[car]
    return dct


def refuel_the_car(dct, info):
    car = info[1]
    fuel = int(info[2])
    if dct[car]["fuel"] + fuel > 75:
        refueled = 75 - dct[car]["fuel"]
        dct[car]["fuel"] = 75
        print(f"{car} refueled with {refueled} liters")
    else:
        dct[car]["fuel"] += fuel
        print(f"{car} refueled with {fuel} liters")
    return dct


def revert(dct, info):
    car = info[1]
    km = int(info[2])
    if dct[car]["mileage"] - km >= 10000:
        dct[car]["mileage"] -= km
        print(f"{car} mileage decreased by {km} kilometers")
    else:
        dct[car]["mileage"] = 10000
    return dct


number_of_cars = int(input())
my_cars = {}

for _ in range(number_of_cars):
    tokens = input().split("|")
    car, mileage, fuel = tokens[0], int(tokens[1]), int(tokens[2])
    my_cars[car] = {"mileage": mileage, "fuel": fuel}

command = input()
while command != "Stop":
    current_command = command.split(" : ")
    action = current_command[0]
    if action == "Drive":
        my_cars = drive_the_car(my_cars, current_command)
    elif action == "Refuel":
        my_cars = refuel_the_car(my_cars, current_command)
    elif action == "Revert":
        my_cars = revert(my_cars, current_command)

    command = input()

for current_car, info in my_cars.items():
    print(f"{current_car} -> Mileage: {my_cars[current_car]['mileage']} kms, "
          f"Fuel in the tank: {my_cars[current_car]['fuel']} lt.")
