budget = float(input())
is_money_enough = False
while True:
    command = input()
    if command == "ACTION":
        is_money_enough = True
        break
    if len(command) <= 15:
        salary = float(input())
        budget -= salary
    else:
        budget *= 0.8
    if budget <= 0:
        break
if is_money_enough:
    print(f"We are left with {budget:.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")