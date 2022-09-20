text = input()
opening_brackets_indices = []
for i in range(len(text)):
    if text[i] == "(":
        opening_brackets_indices.append(i)
    elif text[i] == ")":
        print(text[opening_brackets_indices.pop():i + 1])

