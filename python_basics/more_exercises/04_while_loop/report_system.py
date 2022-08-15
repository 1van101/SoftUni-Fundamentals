expected_sum = int(input())
command = input()
cash_sum = 0
credit_cards_sum = 0
cash_transactions = 0
credit_cards_transactions = 0
counter = 0
while command != "End":
    counter += 1
    if counter % 2 != 0:
        if int(command) > 100:
            print("Error in transaction!")
        else:
            cash_transactions += 1
            cash_sum += int(command)
            print("Product sold!")
    else:
        if int(command) < 10:
            print("Error in transaction!")
        else:
            credit_cards_transactions += 1
            credit_cards_sum += int(command)
            print("Product sold!")

    if cash_sum + credit_cards_sum >= expected_sum:
        print(f"Average CS: {cash_sum / cash_transactions:.2f}")
        print(f"Average CC: {credit_cards_sum / credit_cards_transactions:.2f}")
        break
    command = input()
    if command == "End":
        print("Failed to collect required money for charity.")
        break

# goal = int(input())
# transaction_counter = 0
# cash_counter = 0
# cash_sum = 0
# cc_counter = 0
# cc_sum = 0
# total_sum = cash_sum + cc_sum
# goal_is_reached = False
#
# command = input()
# while command != "End":
#     transaction_counter += 1
#     if transaction_counter % 2 != 0:
#         if int(command) > 100:
#             print("Error in transaction!")
#
#         else:
#             print("Product sold!")
#             cash_counter += 1
#             cash_sum += int(command)
#     else:
#         if int(command) < 10:
#             print("Error in transaction!")
#
#         else:
#             print("Product sold!")
#             cc_counter += 1
#             cc_sum += int(command)
#     if cc_sum + cash_sum >= goal:
#         goal_is_reached = True
#         break
#     command = input()
# if goal_is_reached:
#     print(f"Average CS: {cash_sum / cash_counter:.2f}")
#     print(f"Average CC: {cc_sum / cc_counter:.2f}")
# else:
#     print("Failed to collect required money for charity.")
