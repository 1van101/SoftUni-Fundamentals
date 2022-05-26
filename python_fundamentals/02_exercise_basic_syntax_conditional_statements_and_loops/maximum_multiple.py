division = int(input())
boundary = int(input())
max_num = 0
for i in range(boundary, division, -1):
    if i % division == 0:
        max_num = i
        break
print(max_num)