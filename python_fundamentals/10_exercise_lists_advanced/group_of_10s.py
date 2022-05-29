numbers = [int(x) for x in input().split(", ")]
biggest_num = max(numbers)
group = 10
while len(numbers) > 0:
    current_list = []
    for num in numbers:
        if num <= group:
            current_list.append(num)
    numbers = [x for x in numbers if x not in current_list]
    print(f"Group of {group}'s: {current_list}")
    group += 10