text = input()
phrases = []
numbers = []
current_phrase = ""
current_num = ""

for i in range(len(text)):
    if not text[i].isnumeric():
        current_phrase += text[i].upper()
        if len(current_num) > 0:
            numbers.append(current_num)
            current_num = ""
    else:
        current_num += text[i]
        if len(current_phrase) > 0:
            phrases.append(current_phrase)
            current_phrase = ""
    if i == len(text) - 1:
        numbers.append(current_num)

print(f"Unique symbols used: {len(set(''.join(phrases)))}")
[print(phrases[x] * int(numbers[x]), end="") for x in range(len(phrases))]
