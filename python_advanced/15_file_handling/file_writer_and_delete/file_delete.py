from os import remove, path

absolute_path = path.dirname(path.abspath(__file__))
file_path = path.join(absolute_path, "my_first_file.txt")

try:
    remove(file_path)
except FileNotFoundError:
    print("File already deleted")