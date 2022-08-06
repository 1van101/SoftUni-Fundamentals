num_of_floors = int(input())
num_of_rooms = int(input())

for f in range(num_of_floors, 0, -1):
    for r in range(num_of_rooms):

        if f == num_of_floors:
            print(f"L{f}{r} ", end="")
        elif f % 2 == 0:
            print(f"O{f}{r} ", end="")
        else:
            print(f"A{f}{r} ", end="")

    print()

# floors = int(input())
# apartments = int(input())
#
# for f in range(floors, 0, -1):
#     is_even = False
#     for a in range (apartments):
#         if f == floors:
#             print(f"L{f}{a}", end=" ")
#             continue
#         if f % 2 == 0:
#             is_even = True
#         if is_even:
#             print(f"O{f}{a}", end=" ")
#         else:
#             print(f"A{f}{a}", end=" ")
#
#     print()