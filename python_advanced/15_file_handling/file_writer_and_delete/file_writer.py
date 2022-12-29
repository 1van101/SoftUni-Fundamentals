from os import path

absolute_path = path.dirname(path.abspath(__file__))
file_path = path.join(absolute_path, "my_first_file.txt")

with open(file_path, "w") as file:
    file.write("I just created my first file")
