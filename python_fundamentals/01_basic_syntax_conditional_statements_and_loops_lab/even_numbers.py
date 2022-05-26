lines = int(input())
is_odd = False
last_num = 0
for i in range(lines):
    number = int(input())
    if number % 2 != 0:
        is_odd = True
        last_num = number
        break
if is_odd:
    print(f"{last_num} is odd!")
else:
    print("All numbers are even.")
