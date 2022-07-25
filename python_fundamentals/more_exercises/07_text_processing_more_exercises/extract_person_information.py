def extract_information(current_word, symbol_start, symbol_end):
    start = current_word.index(symbol_start)
    end = current_word.index(symbol_end)
    return current_word[start + 1:end]


n = int(input())
for i in range(n):
    name = None
    age = None
    string = input().split()

    for word in string:
        if "@" in word and "|" in word:
            name = extract_information(word, "@", "|")
        if "#" in word and "*" in word:
            age = extract_information(word, "#", "*")
    print(f"{name} is {age} years old.")