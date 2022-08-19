voucher = int(input())
movie_ticket_counter = 0
food_counter = 0
while True:
    command = input()
    if command == "End":
        break
    if len(command) > 8:
        movie_ticket_counter += 1
        for position, char in enumerate(command):
            if position == 2:
                break
            voucher -= ord(char)
        if voucher < 0:
            movie_ticket_counter -= 1
            break
    else:
        food_counter += 1
        voucher -= ord(command[0])
        if voucher < 0:
            food_counter -= 1
            break

print(f"{movie_ticket_counter}")
print(f"{food_counter}")