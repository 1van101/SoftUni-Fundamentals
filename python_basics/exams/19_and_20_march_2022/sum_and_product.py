n = int(input())
num_is_found = False
num_backward_is_found = False
for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(0, 10):
            for d in range(9, c - 1, -1):
                sum = a + b + c + d
                multiplication = a * b * c * d
                if sum == multiplication and n % 10 == 5:
                    num_is_found = True
                    print(f"{a}{b}{c}{d}")
                    break
                elif multiplication // sum == 3 and n % 3 == 0:
                    num_backward_is_found = True
                    print(f"{d}{c}{b}{a}")
                    break
            if num_is_found or num_backward_is_found:
                break
        if num_is_found or num_backward_is_found:
            break
    if num_is_found or num_backward_is_found:
        break

if num_is_found:
    pass
elif num_backward_is_found:
    pass
else:
    print("Nothing found")