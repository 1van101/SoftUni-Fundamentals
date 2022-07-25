contests_and_pass = {}
contests_with_users = {}

data = input()
while not data == "end of contests":
    cont, psswrd = data.split(":")
    contests_and_pass[cont] = psswrd
    data = input()

command = input()
while not command == "end of submissions":
    tokens = command.split("=>")
    contest, password, username, points = tokens[0], tokens[1], tokens[2], int(tokens[3])
    if contest in contests_and_pass and password == contests_and_pass[contest]:
        if username not in contests_with_users:
            contests_with_users[username] = {contest: points}
        else:
            if contest not in contests_with_users[username]:
                contests_with_users[username][contest] = points
            else:
                if contests_with_users[username][contest] < points:
                    contests_with_users[username][contest] = points

    command = input()

users_with_total_points = {}
for key, value in contests_with_users.items():
    users_with_total_points[key] = sum(value.values())
max_user = max(users_with_total_points.items(), key= lambda x: x[1])

print(f"Best candidate is {max_user[0]} with total {max_user[1]} points.")
print("Ranking:")
contests_with_users_sorted = dict(sorted(contests_with_users.items(), key= lambda x: (x[0])))
for k, v in contests_with_users_sorted.items():
    print(k)
    v_sorted = sorted(v.items(), key= lambda x: -x[1])
    for data in v_sorted:
        print(f"#  {data[0]} -> {data[1]}")