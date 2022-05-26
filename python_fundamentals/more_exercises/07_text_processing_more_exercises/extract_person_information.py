def get_name_and_age(text):
    text = text.split()
    name = ""
    age = ""
    for word in text:
        if "@" in word and "|" in word:
            at_index = word.index("@")
            trait_index = word.index("|")
            name = word[at_index + 1:trait_index]
        if "#" in word and "*" in word:
            sharp_index = word.index("#")
            star_index = word.index("*")
            age = word[sharp_index + 1:star_index]

    return f"{name} is {age} years old."


number = int(input())

for line in range(number):
    data = input()
    print(get_name_and_age(data))