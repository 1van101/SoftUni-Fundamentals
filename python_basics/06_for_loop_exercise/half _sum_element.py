import sys

num = int(input())

max_number = -sys.maxsize
total_sum = 0

for i in range (1, num + 1):
    current_num = int(input())
    if current_num > max_number:
        max_number = current_num
    total_sum = total_sum + current_num

if total_sum - max_number == max_number:
    print ("Yes")
    print(f"Sum = {max_number}")
else:
    difference = abs(max_number - (total_sum - max_number))
    print("No")
    print(f"Diff = {difference}")


