capacity = int(input())
income = 0
tickets_counter = 0
movie_starts = False
is_full = False
while True:
    command = input()
    if command == "Movie time!":
        movie_starts = True
        break

    tickets_counter += int(command)
    if tickets_counter > capacity:
        tickets_counter -= int(command)
        is_full = True
        break
    income += int(command) * 5
    if int(command) % 3 == 0:
        income -= 5
if movie_starts:
    print(f"There are {capacity - tickets_counter} seats left in the cinema.")
if is_full:
    print("The cinema is full.")
print(f"Cinema income - {income} lv.")

# capacity = int(input())
# income_counter = 0
# seats_counter = 0
# movie_starts = False
#
# while True:
#     command = input()
#     if command == "Movie time!":
#         movie_starts = True
#         break
#     capacity -= int(command)
#     if capacity < 0:
#         break
#     income_counter += int(command) * 5
#     if int(command) % 3 == 0:
#         income_counter -= 5
#
# if movie_starts:
#     print(f"There are {capacity} seats left in the cinema.")
# else:
#     print("The cinema is full.")
# print(f"Cinema income - {income_counter} lv.")