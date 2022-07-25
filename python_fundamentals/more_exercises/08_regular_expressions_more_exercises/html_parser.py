import re


def get_title(text):
    matches = re.findall(r"(?<=<title>).*(?=</title>)", text)
    return "".join(matches)


def get_content(text):
    text_body = re.findall(r"<body>.*</body>", text)
    content = re.findall(r">([^><]*)<", "".join(text_body))
    return "".join(content)


text = input()
content = get_content(text).replace('\\n', '')
print(f"Title: {get_title(text)}\nContent: {content}")
