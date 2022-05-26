def get_the_capitals_indices(word):
    list_of_indices = []
    for index, char in enumerate(word):
        if char.isupper():
            list_of_indices.append(index)

    return list_of_indices


single_word = input()
print(get_the_capitals_indices(single_word))