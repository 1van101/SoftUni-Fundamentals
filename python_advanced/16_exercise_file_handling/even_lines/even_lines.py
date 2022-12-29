from os import path
import re


def get_replaced_lines(file, pattern=r'[-,.!?]', new_symbol="@"):
    output = []
    with open(file) as file:
        for line in file:
            new_sentence = re.sub(pattern, new_symbol, line).split()
            output.append(reversed(new_sentence))
    return output


absolute_path = path.dirname(path.abspath(__file__))
file_path = path.join(absolute_path, "text.txt")

replaced_lines = get_replaced_lines(file_path)
[print(' '.join(replaced_lines[x])) for x in range(len(replaced_lines)) if x % 2 == 0]
