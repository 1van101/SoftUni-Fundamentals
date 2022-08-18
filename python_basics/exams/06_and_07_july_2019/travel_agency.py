city = input()
type_equipment = input()
vip_discount = input()
days = int(input())

price = 0
days_are_negative = True
is_invalid_input = False

if days >= 1:
    days_are_negative = False
    if days > 7:
        days -= 1
    if city == "Bansko" or city == "Borovets":
        if type_equipment == "withEquipment":
            price = 100
            if vip_discount == "yes":
                price *= 0.9
        elif type_equipment == "noEquipment":
            price = 80
            if vip_discount == "yes":
                price *= 0.95
        else:
            is_invalid_input = True
    elif city == "Varna" or city == "Burgas":
        if type_equipment == "withBreakfast":
            price = 130
            if vip_discount == "yes":
                price *= 0.88
        elif type_equipment == "noBreakfast":
            price = 100
            if vip_discount == "yes":
                price *= 0.93
        else:
            is_invalid_input = True
    else:
        is_invalid_input = True

if days_are_negative:
    print("Days must be positive number!")
else:
    if is_invalid_input:
        print("Invalid input!")
    else:
        print(f"The price is {price * days:.2f}lv! Have a nice time!")

# city = input()
# type = input()
# vip_discount = input()
# nights = int(input())
# price = 0
# is_negative = False
# is_invalid = False
# if nights > 7:
#     nights -= 1
# elif nights < 1:
#     is_negative = True
# if city == "Bansko" or city == "Borovets":
#     if type == "withEquipment":
#         price = 100
#         if vip_discount == "yes":
#             price *= 0.9
#     elif type == "noEquipment":
#         price = 80
#         if vip_discount == "yes":
#             price *= 0.95
#     else:
#         is_invalid = True
#
# elif city == "Varna" or city == "Burgas":
#     if type == "withBreakfast":
#         price = 130
#         if vip_discount == "yes":
#             price *= 0.88
#     elif type == "noBreakfast":
#         price = 100
#         if vip_discount == "yes":
#             price *= 0.93
#     else:
#         is_invalid = True
# else:
#     is_invalid = True
# total_price = price * nights
# if is_negative:
#     print("Days must be positive number!")
# elif is_invalid:
#     print(f"Invalid input!")
# else:
#     print(f"The price is {total_price:.2f}lv! Have a nice time!")
