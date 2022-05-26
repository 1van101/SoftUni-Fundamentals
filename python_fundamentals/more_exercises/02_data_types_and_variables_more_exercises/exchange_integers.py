def get_exchanged_values(n1, n2):
    n1, n2 = n2, n1
    return f"After: \na = {n1}\nb = {n2}"


first_num = int(input())
second_num = int(input())

print(f"Before: \na = {first_num}\nb = {second_num}")
print(get_exchanged_values(first_num, second_num))