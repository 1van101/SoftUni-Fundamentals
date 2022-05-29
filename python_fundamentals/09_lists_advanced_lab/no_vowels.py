text = input()
vowels_list = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "I"]

filtered_list = [c for c in text if c not in vowels_list]
print("".join(filtered_list))
