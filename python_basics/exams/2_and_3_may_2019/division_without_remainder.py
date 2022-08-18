num = int(input())

p1 = 0
p2 = 0
p3 = 0
for i in range(num):
    current_num = int(input())
    if current_num % 2 == 0:
        p1 += 1
    if current_num % 3 == 0:
        p2 += 1
    if current_num % 4 == 0:
        p3 += 1

print(f"{p1 / num * 100:.2f}%")
print(f"{p2 / num * 100:.2f}%")
print(f"{p3 / num * 100:.2f}%")