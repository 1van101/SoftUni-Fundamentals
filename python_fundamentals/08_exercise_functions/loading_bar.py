def get_loading_bar(num):
    current_num = num // 10
    list_of_symbols = []

    for i in range(current_num):
        list_of_symbols.append("%")

    for j in range(10 - current_num):
        list_of_symbols.append(".")

    list_of_symbols = "".join(list_of_symbols)

    if num == 100:
        return f"100% Complete! \n[{list_of_symbols}]"
    else:
        return f"{num}% [{list_of_symbols}] \nStill loading..."


number = int(input())
loading_bar = get_loading_bar(number)

print(loading_bar)

# ========================================================================================================================
# def loading_bar(number):
#     list_of_symbols = []
#     current_num = number // 10
#     list_of_symbols.append("%" * current_num)
#     list_of_symbols.append("." * (10 - current_num))
#     list_of_symbols_unpacked = "".join(list_of_symbols)
#     if number == 100:
#         return f"100% Complete! \n[{list_of_symbols_unpacked}]"
#     else:
#         return f"{number}% [{list_of_symbols_unpacked}] \nStill loading..."
#
#
#
# num = int(input())
# print(loading_bar(num))