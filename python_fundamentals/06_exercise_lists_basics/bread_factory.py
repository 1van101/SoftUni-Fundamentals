daily_events = input().split("|")
energy = 100
coins = 100
gained = 0

for type in daily_events:
    type = type.split("-")
    event_num = int(type[1])
    event_type = type[0]
    if event_type == "rest":

        if energy == 100:

            print(f"You gained 0 energy.")
            print(f"Current energy: {energy}.")
        else:
            if event_num + energy > 100:
                gained = event_num-(energy + event_num - 100)
                energy = 100
                print(f"You gained {gained} energy.")
                print(f"Current energy: 100.")
            else:
                energy += event_num
                print(f"You gained {event_num} energy.")
                print(f"Current energy: {energy}.")
    elif event_type == "order":
        coins += event_num
        energy -= 30
        if energy >= 0:
            print(f"You earned {event_num} coins.")
        else:
            coins -= event_num
            energy += 80
            print("You had to rest!")
    else:

        if coins >= event_num:
            print(f"You bought {event_type}.")
            coins -= event_num
        else:
            print(f"Closed! Cannot afford {event_type}.")
            exit()
if coins >= 0:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")



