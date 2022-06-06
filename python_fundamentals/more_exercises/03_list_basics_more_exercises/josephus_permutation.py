number_of_people = input().split()
num = int(input())

executed = []
counter = num - 1

while len(number_of_people) > 0:

    while counter >= len(number_of_people):
        counter -= len(number_of_people)

    executed.append(number_of_people.pop(counter))

    counter += num - 1
print(f"[{','.join(executed)}]")
