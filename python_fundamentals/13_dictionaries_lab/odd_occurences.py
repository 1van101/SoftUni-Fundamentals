words = input().split()
words_lower = [x.lower() for x in words]
words_dict = {}

for repeat in words_lower:
    if repeat not in words_dict:
        words_dict[repeat] = 0
    words_dict[repeat] += 1

[print(k, end=" ") for k, v in words_dict.items() if v % 2 != 0]