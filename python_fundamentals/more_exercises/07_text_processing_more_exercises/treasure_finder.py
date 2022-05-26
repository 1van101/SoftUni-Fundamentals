def get_decrypted_message(nums, text):
    decrypted_message = []
    i = 0
    for char in text:
        char_to_num = ord(char) - nums[i]
        decrypted_message.append(chr(char_to_num))
        i += 1
        if i >= len(nums):
            i = 0
    return decrypted_message

def get_type(message):
    type = []
    is_valid = False
    counter = 0
    for index in range(len(message)):
        if message[index] == "&":
            counter = index
            while message[counter + 1] != "&":
                type.append(message[counter + 1])
                counter += 1
            is_valid = True
            break
    if is_valid:
        return type

def get_coordinates(message):
    coordinates = []
    is_valid = False
    counter = 0
    for index in range(len(message)):
        if message[index] == "<":
            counter = index
            while message[counter + 1] != ">":
                coordinates.append(message[counter + 1])
                counter += 1
            is_valid = True
            break
    if is_valid:
        return coordinates


key = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "find":
        break
    message = get_decrypted_message(key, command)
    type = "".join(get_type(message))
    coordinates = "".join(get_coordinates(message))
    print(f"Found {type} at {coordinates}")