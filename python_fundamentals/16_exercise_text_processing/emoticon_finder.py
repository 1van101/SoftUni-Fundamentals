some_text = input()

[print(f":{some_text[x + 1]}") for x in range(len(some_text)) if some_text[x] == ":"]