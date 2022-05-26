n = int(input())
numbers = [5, 7, 11]
for num in range(1, n + 1):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    if sum in numbers:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")


