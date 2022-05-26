import re

lines = int(input())
for i in range(lines):
    current_text = input()
    matches = re.findall(r"^[^.,_]*$", current_text)
    if matches:
        print(f"{''.join(matches)} is pure.")
    else:
        print(f"{current_text} is not pure!")
