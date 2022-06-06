def index_validity(i, ship):
    if 0 <= i < len(ship):
        return True
    return False


def fire_the_warship(i, dmg, w_status):
    if index_validity(i, w_status):
        w_status[i] -= dmg
        if w_status[i] <= 0:
            print("You won! The enemy ship has sunken.")
            exit()
    return w_status


def defend_the_pirate_ship(start, end, dmg, p_status):
    if index_validity(start, p_status) and index_validity(end, p_status):
        for i in range(start, end + 1):
            p_status[i] -= dmg
            if p_status[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()
    return p_status


def repair_the_pirate_ship(i, health, max_health, p_status):
    if index_validity(i, p_status):
        p_status[i] += health
        if p_status[i] > max_health:
            p_status[i] = max_health
    return p_status


def status(max_health, p_status):
    sections_needed_repair = [int(x) for x in p_status if x < max_health * 0.2]
    print(f"{len(sections_needed_repair)} sections need repair.")


pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
health_capacity = int(input())

while True:
    command = input()
    if command == "Retire":
        break
    tokens = command.split()
    action = tokens[0]
    if action == "Fire":
        index = int(tokens[1])
        damage = int(tokens[2])
        warship = fire_the_warship(index, damage, warship)
    elif action == "Defend":
        index_start = int(tokens[1])
        index_end = int(tokens[2])
        damage = int(tokens[3])
        pirate_ship = defend_the_pirate_ship(index_start, index_end, damage, pirate_ship)
    elif action == "Repair":
        index = int(tokens[1])
        health = int(tokens[2])
        pirate_ship = repair_the_pirate_ship(index, health, health_capacity, pirate_ship)
    elif action == "Status":
        status(health_capacity, pirate_ship)

pirate_ship_sum = sum(pirate_ship)
warship_sum = sum(warship)

print(f"Pirate ship status: {pirate_ship_sum}\nWarship status: {warship_sum}")
