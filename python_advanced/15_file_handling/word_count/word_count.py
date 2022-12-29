import re


def count_matches(file):
    for word in words:
        pattern = fr"\b{word}\b"
        matches = re.findall(pattern, file, re.I)
        words_count[word] = len(matches)


with open("words.txt", 'r') as file_words:
    words = file_words.readline().split()
    words_count = {k: 0 for k in file_words.readline().split()}

with open("input.txt", "r") as file_input:
    file = file_input.read()
    count_matches(file)

with open("output.txt", "w") as file_output:
    for k, v in sorted(words_count.items(), key=lambda x: -x[1]):
        file_output.writelines(f"{k} - {v}" + "\n")

# =================================================================================================
# import re
#
#
# def read_searched_words(file_path="words.txt"):
#     with open(file_path) as file:
#         return {word: 0 for word in file.readline().split()}
#
#
# def count_searched_words(words, file_path="input.txt"):
#     with open(file_path, encoding="utf-8") as file:
#         text = file.read()
#         for k in words:
#             pattern = fr"\b{k}\b"
#             matches = re.findall(pattern, text, re.I)
#             words[k] = len(matches)
#     return words
#
#
# def store_result(result, output_file_path="output.txt"):
#     with open(output_file_path, "w") as file:
#         file.writelines((f"{k} - {v}\n" for k, v in sorted(result.items(), key=lambda x: -x[1])))
#
#
# searched_words = read_searched_words()
# searched_words_counted = count_searched_words(searched_words)
# store_result(searched_words_counted)
