def first_letter_result(word):
    num = int(word[1:-1])
    if word[0].isupper():
        return num / (ord(word[0]) - 64)
    else:
        return num * (ord(word[0]) - 96)


def final_result(word):
    first_letter_res = first_letter_result(word)
    if word[-1].isupper():
        total_res = first_letter_res - (ord(word[-1]) - 64)
    else:
        total_res = first_letter_res + (ord(word[-1]) - 96)
    return total_res


words = input().split()
total_result = sum([final_result(x) for x in words])
print(f"{total_result:.2f}")