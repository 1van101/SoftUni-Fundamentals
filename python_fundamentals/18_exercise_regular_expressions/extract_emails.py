import re

text = input()


# pattern = r"(?<=\s)([a-z0-9]+[.\-\_]?[a-z0-9]+)@ \b"
pattern = r"(?<=\s)([a-z0-9]+[.\-\_]?[a-z0-9]+)@([a-z]+)(-[a-z]+)*\.([a-z\.]+)\b"
matches = re.finditer(pattern, text)

# print("\n".join(matches))

for match in matches:
    print(match.group(0))