def get_the_smallest_num(n1, n2, n3):
    return min([n1, n2, n3])


num1 = int(input())
num2 = int(input())
num3 = int(input())

the_smallest_num = get_the_smallest_num(num1, num2, num3)
print(the_smallest_num)