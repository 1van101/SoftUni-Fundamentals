number_of_doubles = int(input())
list_of_all_synonyms = {}
for words in range(number_of_doubles):
    word = input()
    synonym = input()
    if word not in list_of_all_synonyms:
        list_of_all_synonyms[word] = []
    list_of_all_synonyms[word].append(synonym)


for k, v in list_of_all_synonyms.items():
    print(f"{k} - {', '.join(v)}")

