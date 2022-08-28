number_of_clients = int(input())
all_money_spend = 0
for clients in range(number_of_clients):
    products_counter = 0
    current_client_spends = 0
    while True:
        command = input()
        if command == "Finish":

            if products_counter % 2 == 0:
                current_client_spends *= 0.8
                print(f"You purchased {products_counter} items for {current_client_spends:.2f} leva.")
            else:
                print(f"You purchased {products_counter} items for {current_client_spends:.2f} leva.")
            all_money_spend += current_client_spends
            break
        products_counter += 1
        if command == "basket":
            current_client_spends += 1.50
        elif command == "wreath":
            current_client_spends += 3.80
        else:
            current_client_spends += 7


print(f"Average bill per client is: {all_money_spend / number_of_clients:.2f} leva.")