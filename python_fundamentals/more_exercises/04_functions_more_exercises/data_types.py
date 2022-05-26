def get_result(command, value):
    if command == "int":
        return int(value) * 2
    elif command == "real":
        return f"{float(value) * 1.5:.2f}"
    elif command == "string":
        return "$" + value[0::] + "$"


command_input = input()
number_input = input()
print(get_result(command_input, number_input))
