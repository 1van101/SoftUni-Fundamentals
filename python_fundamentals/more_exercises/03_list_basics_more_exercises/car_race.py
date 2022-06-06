def get_time(list):
    sum = 0
    for t in list:
        if t == 0:
            sum *= 0.8
        else:
            sum += t
    return f"{sum:.1f}"


times = [int(x) for x in input().split()]

middle_times = len(times) // 2
left_racer = times[:middle_times]
right_racer = times[:middle_times:-1]

left = get_time(left_racer)
right = get_time(right_racer)

if float(left) < float(right):
    print(f"The winner is left with total time: {left}")
elif float(left) > float(right):
    print(f"The winner is right with total time: {right}")