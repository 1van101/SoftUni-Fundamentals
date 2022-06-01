def data_process(rooms, i):
    com, n = rooms[i].split()
    return com, int(n)


def potion(init_health, curr_health):
    if init_health + curr_health <= 100:
        init_health += curr_health
    else:
        curr_health = 100 - init_health
        init_health = 100
    print(f"You healed for {curr_health} hp.\nCurrent health: {init_health} hp.")
    return init_health


def chest(init_btc, n):
    init_btc += n
    print(f"You found {n} bitcoins.")
    return init_btc


def facing_monster(room, monster, init_health, power):
    if init_health - power > 0:
        init_health -= power
        print(f"You slayed {monster}.")
    else:
        print(f"You died! Killed by {monster}.\nBest room: {room + 1}")
        exit()
    return init_health


def managed_to_go_through_the_rooms(init_btc, init_health):
    print(f"You've made it!\nBitcoins: {init_btc}\nHealth: {init_health}")


initial_health = 100
initial_btc = 0

rooms = input().split("|")

for i in range(len(rooms)):
    command, number = data_process(rooms, i)
    if command == "potion":
        initial_health = potion(initial_health, number)
    elif command == "chest":
        initial_btc = chest(initial_btc, number)
    else:
        initial_health = facing_monster(i, command, initial_health, number)

managed_to_go_through_the_rooms(initial_btc, initial_health)
