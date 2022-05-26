import re

text = input()
pattern = r"\b(\d{2})([.\-\/])([A-Z][a-z]{2})\2([0-9]{4})\b"

matches = re.finditer(pattern, text)

for match in matches:
    match_str = match.group(2)
    print(match_str)