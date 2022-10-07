unique_elements = set()
n = int(input())

for i in range(n):
    elements = input().split()
    unique_elements = unique_elements.union(elements)

print('\n'.join(unique_elements))