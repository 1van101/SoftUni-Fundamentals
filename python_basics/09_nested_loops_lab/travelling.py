while True:
    destination = input()
    if destination == "End":
        break
    budget_needed = float(input())
    while budget_needed > 0:
        save = float(input())
        budget_needed -= save
    print(f"Going to {destination}!")

# destination = input()
# budget_needed = float(input())
#
# savings = 0
#
# while destination != "End":
#     while savings < budget_needed:
#         saved_money = float(input())
#         savings += saved_money
#
#     print(f"Going to {destination}!")
#
#     destination = input()
#     savings = 0
#
#     if destination == "End":
#         break
#
#     budget_needed = float(input())







