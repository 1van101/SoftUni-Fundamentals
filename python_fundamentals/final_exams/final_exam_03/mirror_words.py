import re


def check_for_palindromes(dct, lst):
    for i in range(len(dct["first"])):
        if dct["second"][i] == dct["first"][i][::-1]:
            lst.append(f"{dct['first'][i]} <=> {dct['second'][i]}")
    return lst


secret_message = input()
found_words = {"first": [], "second": []}
palindromes = []
pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
matches = re.finditer(pattern, secret_message)

for match in matches:
    found_words["first"].append(match.group(2))
    found_words["second"].append(match.group(3))

palindromes = check_for_palindromes(found_words, palindromes)

if len(found_words["first"]) > 0:
    print(f"{len(found_words['first'])} word pairs found!")
else:
    print("No word pairs found!")

if len(palindromes) > 0:
    print(f'The mirror words are:\n{", ".join(palindromes)}')
else:
    print("No mirror words!")
