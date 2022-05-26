num = int(input())
sum = 0
for chars in range(num):
    char = input()
    sum += ord(char)
print(f"The sum equals: {sum}")
