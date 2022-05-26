first_symbol = input()
second_symbol = input()
data = input()

total_sum = 0
special_symbols = []

for i in range(ord(first_symbol) + 1, ord(second_symbol)):
    special_symbols.append(chr(i))

for token in data:
    if token in special_symbols:
        total_sum += ord(token)

print(total_sum)