contest_validation = {}
usernames_and_points = {}

while True:
    contest_and_pass = input()
    if contest_and_pass == "end of contests":
        break
    contest, password = contest_and_pass.split(":")
    contest_validation[contest] = password

while True:
    data = input()
    if data == "end of submissions":
        break
    current_contest, current_password, current_username, current_points = data.split("=>")
    current_points = int(current_points)

    for cont, psswrd in contest_validation.items():
        if cont == current_contest and psswrd == current_password:
            if current_username not in usernames_and_points.keys():
                usernames_and_points[current_username] = {current_contest: current_points}
            else:
                if current_contest in usernames_and_points[current_username]:
                    if current_points > usernames_and_points[current_username][current_contest]:
                        usernames_and_points[current_username][current_contest] = current_points
                else:
                    usernames_and_points[current_username][current_contest] = current_points

total_result = {}

for name, name_value in usernames_and_points.items():
    total_result[name] = 0
    for points in name_value.values():
        total_result[name] += points
best_candidate = max(total_result, key=lambda x:total_result[x])
best_result = total_result[best_candidate]

print(f"Best candidate is {best_candidate} with total {best_result} points.")
print("Ranking:")
usernames_and_points_sorted = sorted(usernames_and_points.items(), key=lambda kv: kv [0], reverse=False)

for usernames, values in usernames_and_points_sorted:
    print(f"{usernames}")
    courses_sorted = sorted(values.items(), key=lambda kv:-kv[1])
    for cont, psswrd in courses_sorted:
        print(f"#  {cont} -> {psswrd}")




