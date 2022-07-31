number_tabs = int(input())
salary = int(input())

fine = 0

for i in range(1, number_tabs + 1):
    website_name = input()
    if website_name == "Facebook":
        fine += 150
    elif website_name == "Instagram":
        fine += 100
    elif website_name == "Reddit":
        fine += 50
    if salary - fine <= 0:
        print("You have lost your salary.")
        break
if salary - fine > 0:
    money_left = salary - fine
    print(money_left)
# tabs = int(input())
# salary = int(input())
#
# is_broke = False
#
# for tab in range(tabs):
#     site = input()
#     if site == "Facebook":
#         salary -= 150
#     elif site == "Instagram":
#         salary -= 100
#     elif site == "Reddit":
#         salary -= 50
#     if salary <= 0:
#         is_broke = True
#         break
# if is_broke:
#     print("You have lost your salary.")
# else:
#     print(f"{salary}")

