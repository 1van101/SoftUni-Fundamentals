lines = int(input())
numbers = []
for i in range(lines):
    numbers.append(int(input()))

command = input()
if command == "even":
    res = [x for x in numbers if x % 2 == 0]
elif command == "odd":
    res = [x for x in numbers if x % 2 != 0]
elif command == "negative":
    res = [x for x in numbers if x < 0]
else:
    res = [x for x in numbers if x >= 0]

print(res)