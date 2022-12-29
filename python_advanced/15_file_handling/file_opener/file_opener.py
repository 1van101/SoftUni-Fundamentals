import os

while True:
    file_name = input()
    try:
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(absolute_path, file_name + ".txt")
        file = open(file_path)
        print("File found")
        break
    except FileNotFoundError:
        print("File not found")
        print("Please enter valid file name!")

