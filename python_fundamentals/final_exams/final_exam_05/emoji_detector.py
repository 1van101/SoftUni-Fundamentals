import re


def get_emojis(text):
    emojis = []
    pattern = r"(:|\*){2}([A-Z][a-z]{2,})\1{2}"
    matches = re.finditer(pattern, text)
    for match in matches:
        emojis.append(match.group(0))
    return emojis


def count_cool_threshold(text):
    cool_threshold = 1
    matches = re.findall(r"\d", text)
    for match in matches:
        cool_threshold *= int(match)
    return cool_threshold


text = input()

cool_threshold = count_cool_threshold(text)
emojis = get_emojis(text)

print(f"Cool threshold: {cool_threshold}\n{len(emojis)} emojis found in the text. The cool ones are:")
[print(x) for x in emojis if sum([ord(y) for y in x[2:-2]]) > cool_threshold]
