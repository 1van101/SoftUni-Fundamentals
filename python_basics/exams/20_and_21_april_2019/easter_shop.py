eggs_start = int(input())
eggs_counter = 0
eggs_num_last = 0
eggs_are_finished = False
is_closed = False
while True:
    command = input()
    if command == "Close":
        is_closed = True
        break
    eggs_number = int(input())
    if command == "Buy":
        eggs_counter += eggs_number
    else:
        eggs_start += eggs_number
    if eggs_counter > eggs_start:
        eggs_num_last = eggs_number
        eggs_are_finished = True
        break
diff = abs(eggs_start - eggs_counter)
if is_closed:
    print("Store is closed!")
    print(f"{eggs_counter} eggs sold.")
if eggs_are_finished:
    print("Not enough eggs in store!")
    print(f"You can buy only {eggs_num_last - diff}.")