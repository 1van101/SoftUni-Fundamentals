secret_message = input().split()
secret_message_deciphered = []

for word in secret_message:
    number = ""
    for char in word:
        if char.isdigit():
            number += char
    x = word.replace(number, chr(int(number)))
    secret_message_deciphered.append(x)

for word in range(len(secret_message_deciphered)):
    current_word = list(secret_message_deciphered[word])
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    print("".join(current_word), end=" ")