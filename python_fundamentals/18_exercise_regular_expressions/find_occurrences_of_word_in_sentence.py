import re

text = input()
word = input()

matches = re.findall(rf"(?i)\b{word}\b", text)
# matches = re.findall(fr"\b{word}\b", text, flags = re.I)
print(len(matches))