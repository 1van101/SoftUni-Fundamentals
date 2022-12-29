from os import path
import re

absolute_path = path.dirname(path.abspath(__file__))
file_path = path.join(absolute_path, "text.txt")

with open(file_path, "r") as file, open("./output.txt", "w") as output_file:
    for idx, line in enumerate(file.readlines(), 1):
        letters_number = len(re.findall(r"[A-z]", line))
        punctuation_marks_count = len(re.findall(r"[^\w\s\d]", line))
        output_file.writelines(f"Line {idx}: {line.strip()} ({letters_number})({punctuation_marks_count})" + "\n")
