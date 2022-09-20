brackets = input()
stack = []
open_brackets = ["{", "[", "("]
closed_brackets = ["}", "]", ")"]
is_balanced = True

for bracket in brackets:
    if len(brackets) % 2 != 0:
        is_balanced = False
        break
    if bracket in open_brackets:
        stack.append(open_brackets.index(bracket))
    elif bracket in closed_brackets:
        if stack:
            if closed_brackets.index(bracket) == stack.pop():
                continue

        is_balanced = False
        break

if is_balanced and not stack:
    print("YES")
else:
    print("NO")
