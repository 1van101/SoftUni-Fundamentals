text = input()
filtered_text = text[0]

for char in text:
    if filtered_text[-1] != char:
        filtered_text += char

print(filtered_text)

# ========================================
# text = input()
# filtered_text = ""
# last_letter = ""
#
# for cur_letter in text:
#     if last_letter != cur_letter:
#         filtered_text += cur_letter
#         last_letter = cur_letter
#
# print(filtered_text)