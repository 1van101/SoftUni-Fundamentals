budget = float(input())
num_videocards = int(input())
num_processors = int(input())
num_ram = int(input())

videocards = 250 * num_videocards
processors = videocards * 0.35 * num_processors
ram = videocards * 0.1 * num_ram

total_sum = videocards + processors + ram
if num_videocards > num_processors:
    total_sum *= 0.85

difference = abs(budget - total_sum)

if budget >= total_sum:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")

