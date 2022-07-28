text = list(input())
indices = []
strength = 0

for i in range(len(text)):
    if text[i] == ">":
        strength += int(text[i + 1])
    if strength > 0 and not text[i] == ">":
        strength -= 1
        indices.append(i)

text = [text[i] for i in range(len(text)) if i not in indices]
print("".join(text))

# ===============================
# some_text = input()
# strenght = 0
# filtered_text = []
#
# for s in range(len(some_text)):
#     if some_text[s] != ">" and strenght < 1:
#         filtered_text.append(some_text[s])
#     elif some_text[s] != ">" and strenght >= 1:
#         strenght -= 1
#     elif some_text[s] == ">":
#         filtered_text.append(some_text[s])
#         strenght += int(some_text[s + 1])
#
# print("".join(filtered_text))



