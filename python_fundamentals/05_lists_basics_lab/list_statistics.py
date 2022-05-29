lines = int(input())

list_of_positives = []
list_of_negatives = []

for i in range(lines):
    num = int(input())
    if num >= 0:
        list_of_positives.append(num)
    else:
        list_of_negatives.append(num)

print(list_of_positives)
print(list_of_negatives)
print(f"Count of positives: {len(list_of_positives)}")
print(f"Sum of negatives: {sum(list_of_negatives)}")
