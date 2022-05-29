import re

participants = input().split(", ")
participants_and_results = {}

while True:
    current_name = ""
    current_result = 0
    command = input()
    if command == "end of race":
        break

    matches = re.finditer(r"([A-Za-z])|(\d)", command)
    for match in matches:
        if match.group(1):
            current_name += (match.group(1))
        elif match.group(2):
            current_result += int(match.group(2))

    if current_name in participants:
        if current_name not in participants_and_results:
            participants_and_results[current_name] = 0
        participants_and_results[current_name] += current_result

participants_and_results_sorted = sorted(participants_and_results.items(), key=lambda kv: -kv[1])

print(f"1st place: {participants_and_results_sorted[0][0]}")
print(f"2nd place: {participants_and_results_sorted[1][0]}")
print(f"3rd place: {participants_and_results_sorted[2][0]}")
