from os import path

absolute_path = path.dirname(path.abspath(__file__))
file_path = path.join(absolute_path, "numbers.txt")


try:
    with open(file_path, "r") as file:
        print(sum([int(x) for x in file.readlines()]))
except FileNotFoundError:
    print("Please enter valid file name")
