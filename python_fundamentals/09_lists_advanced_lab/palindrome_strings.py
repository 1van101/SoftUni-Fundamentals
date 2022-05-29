words_list = input().split()
palindrome_input = input()

list_with_palindromes = []
for word in words_list:
    if word == word[::-1]:
        list_with_palindromes.append(word)

number = list_with_palindromes.count(palindrome_input)

print(list_with_palindromes)
print(f"Found palindrome {number} times")