from os import remove


def create_file(file_name):
    open(file_name, "w").close()


def add_to_file(file_name, content):
    with open(file_name, "a") as file:
        file.writelines(content + "\n")


def replace_occurrences(file_name, old, new):
    try:
        with open(file_name, "r+") as file:
            text = file.read().replace(old, new)
            file.seek(0)
            file.truncate()
            file.writelines(text)
    except FileNotFoundError:
        print("An error occurred")


def delete_file(file_path):
    try:
        remove(file_path)
    except FileNotFoundError:
        print("An error occurred")


while True:
    command = input()
    if command == "End":
        break

    command_parts = command.split('-')

    if command_parts[0] == "Create":
        file = command_parts[1]
        create_file(file)
    elif command_parts[0] == "Add":
        file, content = command_parts[1:]
        add_to_file(file, content)
    elif command_parts[0] == "Replace":
        file, old_str, new_str = command_parts[1:]
        replace_occurrences(file, old_str, new_str)
    elif command_parts[0] == "Delete":
        file = command_parts[1]
        delete_file(file)
