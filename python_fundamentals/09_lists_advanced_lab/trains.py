def add_people(wagons, data):
    people = int(data[1])
    wagons[-1] += people
    return wagons


def insert_people(wagons, data):
    i = int(data[1])
    people = int(data[2])
    wagons[i] += people
    return wagons


def leave_the_wagon(wagons, data):
    i = int(data[1])
    people = int(data[2])
    wagons[i] -= people
    return wagons


number_of_wagons = int(input())
wagons_list = [0] * number_of_wagons

command = input()

while command != "End":
    current_command = command.split()
    action = current_command[0]
    if action == "add":
        wagons_list = add_people(wagons_list, current_command)
    elif action == "insert":
        wagons_list = insert_people(wagons_list, current_command)
    elif action == "leave":
        wagons_list = leave_the_wagon(wagons_list, current_command)

    command = input()

print(wagons_list)
