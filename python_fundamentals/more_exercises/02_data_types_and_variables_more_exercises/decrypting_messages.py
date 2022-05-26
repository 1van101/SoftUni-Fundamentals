# key = int(input())
# lines = int(input())
#
# secret_message = []
#
# for char in range(lines):
#     char_input = input()
#     secret_message.append(ord(char_input) + key)
#
# for num in secret_message:
#     print(chr(num), end="")


key = int(input())
lines = int(input())

secret_message = []

for char in range(lines):
    char_input = input()
    secret_message.append(ord(char_input) + key)

secret_message_decrypted = [chr(x) for x in secret_message]
print("".join(secret_message_decrypted))