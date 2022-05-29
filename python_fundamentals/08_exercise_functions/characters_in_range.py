def chars_in_range(first, second):
    symbols_list = []
    for i in range(ord(first) + 1, ord(second)):
        symbols_list.append(chr(i))
    return symbols_list


char1 = input()
char2 = input()
result = chars_in_range(char1, char2)
print(" ".join(result))