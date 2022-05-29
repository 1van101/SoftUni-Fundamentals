number = int(input())

wagons_list = [0] * number

while True:
    command = input()

    if command == "End":
        break

    command_as_list = command.split()
    first_num = int(command_as_list[1])

    if "add" in command:
        wagons_list[-1] += first_num
    elif "insert" in command:
        second_num = int(command_as_list[2])
        wagons_list[first_num] += second_num
    elif "leave" in command:
        second_num = int(command_as_list[2])
        wagons_list[first_num] -= second_num

print(wagons_list)
