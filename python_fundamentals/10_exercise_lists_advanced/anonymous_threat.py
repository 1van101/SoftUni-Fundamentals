text = input().split()

while True:
    command_input = input().split()
    if "3:1" in command_input:
        break

    command = command_input[0]
    if command == "merge":
        start_index = int(command_input[1])
        if start_index < 0:
            start_index = 0
        end_index = int(command_input[2])
        if end_index > len(text):
            end_index = len(text)
            if start_index >= end_index:
                continue
        text[start_index : end_index + 1] = ["".join(text[start_index : end_index + 1])]
    elif command == "divide":
        index = int(command_input[1])
        partitions = int(command_input[2])
        word = text[index]
        new_word = []
        counter = 0
        for i in range(partitions):
            if i == partitions - 1:
                new_word.append(word[counter::])
                break
            new_word.append(word[counter:counter + (len(word) // partitions)])
            counter += len(word) // partitions

        text.pop(index)
        for i in range(len(new_word)):
            text.insert(index + i, new_word[i])

print(" ".join(text))


