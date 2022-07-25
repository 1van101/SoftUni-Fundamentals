def get_decrypted_message(key, mssg):
    decrypted_message = []
    for i in range(len(mssg)):
        decrypted_message.append(chr(ord(mssg[i]) - key[i % len(key)]))
    return ''.join(decrypted_message)


def get_data(mssg):
    type_indices = []
    coordinates_indices = []
    for i in range(len(mssg)):
        if mssg[i] == "&":
            type_indices.append(i)
        elif mssg[i] == "<":
            coordinates_indices.append(i)
        elif mssg[i] == ">":
            coordinates_indices.append(i)

    type = mssg[type_indices[0] + 1:type_indices[1]]
    coordinates = mssg[coordinates_indices[0] + 1:coordinates_indices[1]]
    return type, coordinates


key = [int(x) for x in input().split()]

while True:
    command = input()
    if command == "find":
        break
    message = get_decrypted_message(key, command)
    type, coordinates = get_data(message)
    print(f"Found {type} at {coordinates}")
