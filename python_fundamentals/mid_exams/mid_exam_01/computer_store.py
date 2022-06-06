counter = 0
is_invalid_order = False
total_price_without_taxes = 0

while True:
    command = input()
    counter += 1

    if command == "special" or command == "regular":
        if counter == 1:
            is_invalid_order = True
            break
        break
    if float(command) < 0:
        print("Invalid price!")
    elif float(command) == 0:
        print("Invalid order!" )
    else:
        total_price_without_taxes += float(command)

if is_invalid_order:
    print(f"Invalid order!")
else:
    taxes = total_price_without_taxes * 0.2
    final_price = total_price_without_taxes + taxes
    if command == "special":
        final_price *= 0.9
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_price_without_taxes:.2f}$\nTaxes: {taxes:.2f}$\n-----------\nTotal price: {final_price:.2f}$")