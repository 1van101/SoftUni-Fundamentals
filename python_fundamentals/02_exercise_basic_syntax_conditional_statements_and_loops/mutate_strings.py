first = input()
second = input()
last_word = first
for i in range(len(first)):
    left_side = second[:i + 1]
    right_side = first[i + 1:]

    new_word = left_side + right_side
    if new_word == last_word:
        continue
    else:
        last_word = new_word
        print(new_word)

