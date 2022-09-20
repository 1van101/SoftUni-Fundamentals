from collections import deque


def seconds_to_hours(seconds):
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


robots = [[y for y in x.split('-')] for x in input().split(";")]
robots_with_time = {x: int(y) for x, y in robots}
busy_until_robots = {x: 0 for x in robots_with_time.keys()}

starting_time = input().split(":")
total_time_sec = int(starting_time[-1]) + (int(starting_time[-2]) * 60) + (int(starting_time[-3]) * 3600)
products = deque()

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    total_time_sec += 1
    current_product = products.popleft()
    for robot, busy_until in busy_until_robots.items():
        if total_time_sec >= busy_until:
            busy_until_robots[robot] = total_time_sec + robots_with_time[robot]
            print(f'{robot} - {current_product} [{seconds_to_hours(total_time_sec)}]')
            break
    else:
        products.append(current_product)
