eggs_size = input()
eggs_color = input()
egg_lots = int(input())
price = 0
if eggs_size == "Large":
    if eggs_color == "Red":
        price = 16
    elif eggs_color == "Green":
        price = 12
    else:
        price = 9
elif eggs_size == "Medium":
    if eggs_color == "Red":
        price = 13
    elif eggs_color == "Green":
        price = 9
    else:
        price = 7
else:
    if eggs_color == "Red":
        price = 9
    elif eggs_color == "Green":
        price = 8
    else:
        price = 5
total_price = price * egg_lots * 0.65
print(f"{total_price:.2f} leva.")
