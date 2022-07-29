def drive_the_car(dct, car, distance, fuel):
    if dct[car]['fuel'] < fuel:
        print("Not enough fuel to make that ride")
    else:
        dct[car]['mileage'] += distance
        dct[car]['fuel'] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
    if dct[car]['mileage'] >= 100000:
        del dct[car]
        print(f"Time to sell the {car}!")
    return dct


def refill_the_tank(dct, car, fuel):
    if dct[car]["fuel"] + fuel > 75:
        print(f"{car} refueled with {75 - dct[car]['fuel']} liters")
        dct[car]["fuel"] = 75
    else:
        dct[car]["fuel"] += fuel
        print(f"{car} refueled with {fuel} liters")
    return dct


def decrease_car_mileage(dct, car, kms):
    if dct[car]["mileage"] - kms < 10000:
        dct[car]["mileage"] = 10000
    else:
        dct[car]["mileage"] -= kms
        print(f"{car} mileage decreased by {kms} kilometers")
    return dct


num_of_cars = int(input())

cars = {}

for i in range(num_of_cars):
    car, mileage, fuel = input().split("|")
    cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}

command = input()
while not command == "Stop":
    command = command.split(" : ")
    action = command[0]
    if action == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        cars = drive_the_car(cars, car, distance, fuel)
    elif action == "Refuel":
        car = command[1]
        fuel = int(command[2])
        cars = refill_the_tank(cars, car, fuel)
    elif action == "Revert":
        car = command[1]
        kilometers = int(command[2])
        cars = decrease_car_mileage(cars, car, kilometers)
    command = input()

for car in cars.keys():
    print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")