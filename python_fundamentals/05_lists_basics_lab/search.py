number = int(input())
word = input()
full_list = []

for i in range(number):
    sentence = input()
    full_list.append(sentence)

print(full_list)
filtered_list = [x for x in full_list if word in x]
print(filtered_list)
