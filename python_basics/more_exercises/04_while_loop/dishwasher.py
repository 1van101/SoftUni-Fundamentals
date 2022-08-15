bottles_detergent = int(input())
command = input()

ml_detergent = bottles_detergent * 750
dishes_counter = 0
pots_counter = 0
filling_counter = 0

while command != "End":
    filling_counter += 1
    if filling_counter % 3 == 0:
        pots_counter += int(command)
        ml_detergent -= int(command) * 15
    else:
        dishes_counter += int(command)
        ml_detergent -= int(command) * 5
    if ml_detergent < 0:
        print(f"Not enough detergent, {abs(ml_detergent)} ml. more necessary!")
        break
    command = input()
if command == "End":
    print("Detergent was enough!")
    print(f"{dishes_counter} dishes and {pots_counter} pots were washed.")
    print(f"Leftover detergent {ml_detergent} ml.")

# bottles_of_detergent = int(input())
# total_detergent = bottles_of_detergent * 750
# command = input()
# dishes_counter = 0
# pot_counter = 0
# day_counter = 0
# detergent_not_enough = False
# while command != "End":
#     day_counter += 1
#     if day_counter % 3 == 0:
#         total_detergent -=  int(command) * 15
#         pot_counter += int(command)
#     else:
#         total_detergent -= int(command) * 5
#         dishes_counter += int(command)
#     if total_detergent < 0:
#         detergent_not_enough = True
#         break
#     command = input()
# if detergent_not_enough:
#     print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")
# else:
#     print("Detergent was enough!")
#     print(f"{dishes_counter} dishes and {pot_counter} pots were washed.")
#     print(f"Leftover detergent {total_detergent} ml.")

