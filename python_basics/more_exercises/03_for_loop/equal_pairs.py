pairs = int(input())
num_a = int(input())
num_b = int(input())
result = num_b + num_a
diff = 0
valid = True

for i in range(pairs - 1):
    num_a = int(input())
    num_b = int(input())

    current_result = num_b + num_a

    if current_result != result:
        valid = False
        current_diff = abs(current_result - result)
        result = current_result
        if current_diff > diff:
            diff = current_diff

if valid:
    print(f"Yes, value={result}")
else:
    print(f"No, maxdiff={diff}")



