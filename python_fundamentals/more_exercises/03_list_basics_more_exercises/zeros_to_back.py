current_list = input().split(", ")

new_list = [int(x) for x in current_list if x != "0"]
diff = len(current_list) - len(new_list)

for i in range(diff):
    new_list.append(0)

print(new_list)
