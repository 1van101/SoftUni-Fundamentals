money_needed = float(input())
savings = float(input())
days_passed = 0
spending_counter = 0
spending_too_many_days = False

while savings < money_needed:
    days_passed += 1
    action = input()
    current_money = float(input())
    if action == "spend":
        spending_counter += 1
        savings -= current_money
        if savings < 0:
            savings = 0
        if spending_counter == 5:
            spending_too_many_days = True
            break
    else:
        spending_counter = 0
        savings += current_money

if spending_too_many_days:
    print("You can't save the money.")
    print(days_passed)
else:
    print(f"You saved the money for {days_passed} days.")


