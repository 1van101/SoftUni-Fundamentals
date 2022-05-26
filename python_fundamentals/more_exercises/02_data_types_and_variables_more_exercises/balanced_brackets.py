def check_balanced_or_not(list):
    if len(list) % 2 == 0:
        for symbol in range(len(list)):
            if symbol % 2 == 0 and list[symbol] != "(":
                return "UNBALANCED"
            elif symbol % 2 != 0 and list[symbol] != ")":
                return "UNBALANCED"
        return "BALANCED"
    else:
        return "UNBALANCED"


lines = int(input())
brackets = []
for i in range(lines):
    brackets.append(input())
    brackets = [x for x in brackets if x in("(", ")")]

print(check_balanced_or_not(brackets))


# lines = int(input())
# brackets = []
# for i in range(lines):
#     current_line = input()
#     if current_line == "(" or current_line == ")":
#         brackets.append(current_line)
# is_balanced = True
#
# for symbol in range(len(brackets)):
#     if len(brackets) % 2 == 0:
#         if symbol % 2 == 0 and brackets[symbol] != "(":
#             is_balanced = False
#         elif symbol % 2 != 0 and brackets[symbol] != ")":
#             is_balanced = False
#     else:
#         is_balanced = False
#
# if is_balanced:
#     print("BALANCED")
# else:
#     print("UNBALANCED")