budget = float(input())
total_spends = 0
flour_price = float(input())
pack_of_eggs = flour_price * 0.75
milk_price = flour_price * 1.25 / 4
colored_eggs_counter = 0
bread_counter = 0

while True:

    total_spends += (flour_price + pack_of_eggs + milk_price)
    if total_spends >= budget:
        total_spends -= (flour_price + pack_of_eggs + milk_price)
        break
    bread_counter += 1
    colored_eggs_counter += 3
    if bread_counter % 3 == 0:
        colored_eggs_counter = colored_eggs_counter - (bread_counter - 2)
print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget - total_spends:.2f}BGN left.")