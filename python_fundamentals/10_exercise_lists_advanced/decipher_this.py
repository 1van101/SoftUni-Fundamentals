def number_to_char(mssg):
    number = ""
    for char in mssg:
        if char.isdigit():
            number += char
    mssg = mssg.replace(number, chr(int(number)))
    return mssg


def switch_chars(mssg):
    word_with_switched_chars = list(mssg)
    word_with_switched_chars[1], word_with_switched_chars[-1] = word_with_switched_chars[-1], word_with_switched_chars[1]
    return "".join(word_with_switched_chars)


text = input().split()
text_deciphered = []

for word in text:
    word = number_to_char(word)
    text_deciphered.append(switch_chars(word))

print(" ".join(text_deciphered))
