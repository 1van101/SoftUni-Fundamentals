budget = int(input())
went_in_overdraft = False
while True:
    command = input()
    if command == "End":
        break
    budget -= int(command)
    if budget < 0:
        went_in_overdraft = True
        break

if went_in_overdraft:
    print("You went in overdraft!")
else:
    print("You bought everything needed.")


