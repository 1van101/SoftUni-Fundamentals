results = {}

while True:
    command = input()
    if command == "no more time":
        break
    username, contest, points = command.split(" -> ")
    points = int(points)

    if contest not in results.keys():
        results[contest] = {username: points}
    else:
        if username not in results[contest].keys():
            results[contest][username] = points
        else:
            if points > results[contest][username]:
                results[contest][username] = points

for cont, name_and_points in results.items():
    print(f"{cont}: {len(name_and_points)} participants")
    num = 1
    name_and_points_sorted = sorted(name_and_points.items(), key=lambda kvpt: (-kvpt[1], kvpt[0]))
    for name, points in name_and_points_sorted:
        print(f"{num}. {name} <::> {points}")
        num += 1

print("Individual standings:")
individual_standings = {}
for cont, name_and_points in results.items():
    for name, points in name_and_points.items():
        if name not in individual_standings:
            individual_standings[name] = points
        else:
            individual_standings[name] += points

number = 1

individual_standings_sorted = sorted(individual_standings.items(), key=lambda kvpt: (-kvpt[1], kvpt[0]))
for k, v in individual_standings_sorted:
    print(f"{number}. {k} -> {v}")
    number += 1
