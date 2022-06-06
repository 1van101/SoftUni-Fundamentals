numbers = input().split()
message_input = input()
final_message = []

for current_num in numbers:
    current_result = 0
    for num in current_num:
        current_result += int(num)
    while current_result >= len(message_input):
        current_result -= len(message_input)

    final_message.append(message_input[current_result])
    message_input = message_input[:current_result] + message_input[current_result + 1:]

print("".join(final_message))
