import re

line = input()
numbers = []
while True:
    if line:
        matches = re.finditer(r"\d+", line)
        for match in matches:
            numbers.append(match.group(0))
        line = input()
    else:
        break

print(" ".join(numbers))