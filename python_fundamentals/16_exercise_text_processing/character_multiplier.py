def multiplication(word1, word2):
    return sum([ord(x) * ord(y) for x, y in list(zip(word1, word2))])


def adding(longer_word, shorter_word):
    return sum([ord(x) for x in longer_word[len(shorter_word):]])


first, second = input().split()
total_sum = 0
if len(first) > len(second):
    total_sum = multiplication(first, second) + adding(first, second)
elif len(first) < len(second):
    total_sum = multiplication(first, second) + adding(second, first)
else:
    total_sum = multiplication(first, second)

print(total_sum)