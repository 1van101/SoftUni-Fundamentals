goal = float(input())
command = input()
income = 0
goal_is_reached = False
while command != "Party!":
    number_coctails = int(input())
    coctail_price = len(command)
    current_income = number_coctails * coctail_price
    if current_income % 2 != 0:
        current_income *= 0.75
    income += current_income
    if income >= goal:
        goal_is_reached = True
        break

    command = input()

if goal_is_reached:
    print("Target acquired.")
else:
    print(f"We need {abs(goal - income):.2f} leva more.")
print(f"Club income - {income:.2f} leva.")

# goal = float(input())
# party_starts = False
# income = 0
# while True:
#     cocktail = input()
#     if cocktail == "Party!":
#         party_starts = True
#         break
#     cocktails_number = int(input())
#     current_sum = len(cocktail) * cocktails_number
#     if current_sum % 2 != 0:
#         current_sum *= 0.75
#     income += current_sum
#     if income >= goal:
#         break
# diff = abs(goal - income)
# if party_starts:
#     print(f"We need {diff:.2f} leva more.")
# else:
#     print(f"Target acquired.")
# print(f"Club income - {income:.2f} leva.")