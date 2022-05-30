input_string = input().split()
bakery = {}
for i in range(0, len(input_string), 2):
    key = input_string[i]
    value = input_string[i + 1]
    bakery[key] = int(value)

print(bakery)