num = int(input())

sum_even = 0
sum_odd = 0

for i in range(1, num + 1):
    value = int(input())
    if i % 2 == 0:
        sum_even += value
    else:
        sum_odd += value

difference = abs(sum_odd - sum_even)

if sum_even == sum_odd:
    print("Yes")
    print(f"Sum = {sum_even}")
else:
    print("No")
    print(f"Diff = {difference}")