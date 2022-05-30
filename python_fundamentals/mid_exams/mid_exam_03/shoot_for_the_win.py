def shoot_to_the_target(numbers):
    index = int(command)
    if index < len(numbers) and index not in shot_indexes:
        shot_indexes.append(index)

        for i in range(len(numbers)):
            if i != index and i not in shot_indexes:
                if numbers[i] > numbers[index]:
                    numbers[i] -= numbers[index]
                else:
                    numbers[i] += numbers[index]
        numbers[index] = -1
    return numbers


values_of_the_target = [int(x) for x in input().split()]
command = input()

shot_indexes = []

while command != "End":
    values_of_the_target = shoot_to_the_target(values_of_the_target)

    command = input()

print(f"Shot targets: {len(shot_indexes)} -> {' '.join(str(x) for x in values_of_the_target)}")



