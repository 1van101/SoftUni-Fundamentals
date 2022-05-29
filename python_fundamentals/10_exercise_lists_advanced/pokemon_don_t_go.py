numbers = [int(x) for x in input().split()]

sum = 0

while len(numbers) > 0:
    index = int(input())
    if index < 0:
        popped_num = numbers.pop(0)
        numbers.insert(0, numbers[-1])
        numbers = [(x + popped_num) if x <= popped_num else (x - popped_num) for x in numbers]
        sum += popped_num
    elif index >= len(numbers):
        popped_num = numbers.pop(-1)
        numbers.insert(len(numbers), numbers[0])
        numbers = [(x + popped_num) if x <= popped_num else (x - popped_num) for x in numbers]
        sum += popped_num
    else:
        popped_num = numbers.pop(index)
        numbers = [(x + popped_num) if x <= popped_num else (x - popped_num) for x in numbers]
        sum += popped_num

print(sum)