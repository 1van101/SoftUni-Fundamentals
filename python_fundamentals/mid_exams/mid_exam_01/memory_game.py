elements = input().split()
moves_counter = 0
you_won = False
while True:
    current_elements = []
    index_input =input().split()
    moves_counter += 1
    if "end" in index_input:
        break

    first_index = int(index_input[0])
    second_index = int(index_input[1])
    if first_index == second_index or (first_index >= len(elements) or second_index >= len(elements) or first_index < 0 or second_index < 0):
        elements.insert(len(elements) // 2, f"-{moves_counter}a")
        elements.insert(len(elements) // 2, f"-{moves_counter}a")
        print("Invalid input! Adding additional elements to the board")
    elif elements[first_index] == elements[second_index]:
        current_elements.append(elements[first_index])
        current_elements.append((elements[second_index]))
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")

        elements = [x for x in elements if x not in current_elements]
    elif elements[first_index] != elements[second_index]:
        print("Try again!")
    if len(elements) == 0:
        you_won = True
        break
current_elements = " ".join(elements)

if you_won:
    print(f"You have won in {moves_counter} turns!")
else:
    print(f"Sorry you lose :(\n{current_elements}")