char_start = input()
char_end = input()
char_excluded = input()

def char_range(char_start, char_end):
    for char in range(ord(char_start), ord(char_end) + 1):
        yield chr(char)
counter = 0
for c1 in char_range(char_start, char_end):
    for c2 in char_range(char_start, char_end):
        for c3 in char_range(char_start, char_end):
            if c1 == char_excluded or c2 == char_excluded or c3 == char_excluded:
                pass
            else:
                counter += 1
                print(f"{c1}{c2}{c3}", end=" ")
print(counter, end="")
# letter_min = input()
# letter_max = input()
# letter_except = input()
# counter = 0
# for first_letter in range(ord(letter_min), ord(letter_max) + 1):
#     if first_letter != ord(letter_except):
#         for second_letter in range(ord(letter_min), ord(letter_max) + 1):
#             if second_letter != ord(letter_except):
#                 for third_letter in range(ord(letter_min), ord(letter_max) + 1):
#                     if third_letter != ord(letter_except):
#                         counter += 1
#                         print(f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}", end=" ")
# print(counter)