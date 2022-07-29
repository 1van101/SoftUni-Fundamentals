import re


def get_cool_threshold(text):
    matches = re.findall(r"\d", text)
    cool_threshold = 1
    for num in matches:
        cool_threshold *= int(num)
    return cool_threshold


def get_matched_emojis(text):
    valid_emojis = re.findall(r"(::|\*\*)([A-Z][a-z]{2,})(\1)", text)
    return valid_emojis


text = input()
cool_threshold = get_cool_threshold(text)
matched_emojis = get_matched_emojis(text)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(matched_emojis)} emojis found in the text. The cool ones are:")
[print(''.join(x)) for x in matched_emojis if sum(ord(y) for y in x[1]) > cool_threshold]
