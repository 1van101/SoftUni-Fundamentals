import re

text = input()
pattern = r'(\+359)( |-)2(\2)(\d{3})(\2)(\d{4})\b'
matches = re.finditer(pattern, text)

phone_nums = []

for match in matches:
    match_str = match.group(0)
    phone_nums.append(match_str)

print(', '.join(phone_nums))

