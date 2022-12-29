import os

# absolute_path = os.path.dirname(os.path.abspath(__file__))
#
# file_path = os.path.join(absolute_path, "example.txt")
# file = open(file_path)
# print(file.readlines())

import json

file = open("example.json")    #-> with open("example.json") as file: ->print(file.read())  NO NEED TO CLOSE THE FILE
my_dict = json.load(file)
print(my_dict)
file.close()


#append mode - open and write with no overwriting! : mode = "a"
