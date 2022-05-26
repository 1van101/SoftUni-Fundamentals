import re

emails = []
text = input()
while True:
    if text:
        matches = re.finditer(r"(www.[A-Za-z0-9\-]+\.([a-z.]+))", text)
        for match in matches:
            emails.append(match.group(0))
        text = input()
    else:
        break

[print(x) for x in emails]
