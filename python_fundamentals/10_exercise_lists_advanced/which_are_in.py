first_string = input().split(", ")
second_string = input().split(", ")

filtered_string = []

for first_word in first_string:
    for second_word in second_string:
        if first_word in second_word and first_word not in filtered_string:
            filtered_string.append(first_word)

print(filtered_string)