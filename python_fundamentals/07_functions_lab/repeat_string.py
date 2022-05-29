string = input()
counter = int(input())

repeat_str = lambda s, c: s * c

print(repeat_str(string, counter))

#==========================
# string = input()
# counter = int(input())
# [print(x * counter, end="") for x in string]