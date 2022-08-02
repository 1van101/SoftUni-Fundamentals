username = input()
reg_password = input()

current_password = input()

while current_password != reg_password:
    current_password = input()

print(f"Welcome {username}!")