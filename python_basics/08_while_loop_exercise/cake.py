cake_width = int(input())
cake_lenght = int(input())

pieces = cake_lenght * cake_width
pieces_counter = 0
cake_is_not_over = False

pieces_taken = input()

while pieces > pieces_counter:
    if pieces_taken == "STOP":
        cake_is_not_over = True
        break
    pieces_counter += int(pieces_taken)
    if pieces_counter >= pieces:
        break

    pieces_taken = input()

difference = abs(pieces - pieces_counter)
if cake_is_not_over:
    print(f"{difference} pieces are left.")
else:
    print(f"No more cake left! You need {difference} pieces more.")


# cake_lenght = int(input())
# cake_width = int(input())
# cake_pieces = cake_width * cake_lenght
# pieces_counter = 0
#
# is_cake_over = False
#
# command = input()
# while command != "STOP":
#     pieces_counter += int(command)
#     if pieces_counter >= cake_pieces:
#         is_cake_over = True
#         break
#     command = input()
# diff = abs(cake_pieces - pieces_counter)
# if is_cake_over:
#     print(f"No more cake left! You need {diff} pieces more.")
# else:
#     print(f"{diff} pieces are left.")



