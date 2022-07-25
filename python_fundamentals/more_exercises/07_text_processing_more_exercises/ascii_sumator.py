start = ord(input())
end = ord(input())
string = input()

total_sum = sum([ord(x) for x in string if ord(x) in range(start + 1, end)])

print(total_sum)
