num = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, num + 1):
    count_numbers = int(input())
    if count_numbers < 200:
        p1 += 1
    elif count_numbers < 400:
        p2 += 1
    elif count_numbers < 600:
        p3 += 1
    elif count_numbers < 800:
        p4 += 1
    else:
        p5 += 1

# p1_percent = p1 / num * 100
# p2_percent = p2 / num * 100
# p3_percent = p3 / num * 100
# p4_percent = p4 / num * 100
# p5_percent = p5 / num * 100
print(f"{p1 / num * 100:.2f}%")
print(f"{p2 / num * 100:.2f}%")
print(f"{p3 / num * 100:.2f}%")
print(f"{p4 / num * 100:.2f}%")
print(f"{p5 / num * 100:.2f}%")