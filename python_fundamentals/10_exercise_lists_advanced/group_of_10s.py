numbers = [int(x) for x in input().split(", ")]
boundary = 10

while len(numbers) > 0:
    current_numbers = [x for x in numbers if x <= boundary]
    numbers = [x for x in numbers if x not in current_numbers]

    print(f"Group of {boundary}'s: {current_numbers}")
    boundary += 10
