contribution = input()

balance = 0

while contribution != "NoMoreMoney":
    amount = float(contribution)
    if amount < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {amount:.2f}")
    balance += amount
    contribution = input()

print(f"Total: {balance:.2f}")
# command = input()
# result = 0
#
# while command != "NoMoreMoney":
#     if float(command) < 0:
#         print("Invalid operation!")
#         break
#     result += float(command)
#     print(f"Increase: {command}")
#     command = input()
# print(f"Total: {result}")
