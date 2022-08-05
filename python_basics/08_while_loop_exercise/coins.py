coins = float(input())

coins = int(coins * 100)
change_counter = 0
# change_counter += coins // 200
# coins = coins % 200
# change_counter += coins // 100
# coins = coins % 100
# change_counter += coins // 50
# coins = coins % 50
# change_counter += coins // 20
# coins = coins % 20
# change_counter += coins // 10
# coins = coins % 10
# change_counter += coins // 5
# coins = coins % 5
# change_counter += coins // 2
# coins = coins % 2
# change_counter += coins // 1
# coins = coins % 1
while coins > 0:
    if coins >= 200:
        change_counter += 1
        coins -= 200
    elif coins >= 100:
        change_counter += 1
        coins -= 100
    elif coins >= 50:
        change_counter += 1
        coins -= 50
    elif coins >= 20:
        change_counter += 1
        coins -= 20
    elif coins >= 10:
        change_counter += 1
        coins -= 10
    elif coins >= 5:
        change_counter += 1
        coins -= 5
    elif coins >= 2:
        change_counter += 1
        coins -= 2
    elif coins >= 1:
        change_counter += 1
        coins -= 1

print(change_counter)
