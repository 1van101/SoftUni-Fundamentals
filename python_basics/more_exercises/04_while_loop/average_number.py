num = int(input())
sum = 0
for i in range(num):
    current_num = int(input())
    sum += current_num

print(f"{sum / num:.2f}")