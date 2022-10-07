from collections import deque


def add_to_colors(collected, required, first, second):
    if first in required:
        collected.append(first)
    elif second in required:
        collected.append(second)
    return collected


text = deque(input().split())

main_colors = ['red', 'yellow', 'blue']

secondary_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}
collected_colors = []
while len(text) > 1:
    first_part = text.popleft()
    second_part = text.pop()
    word_first = first_part + second_part
    word_second = second_part + first_part
    if word_first in main_colors or word_second in main_colors:
        collected_colors = add_to_colors(collected_colors, main_colors, word_first, word_second)
    elif word_first in secondary_colors or word_second in secondary_colors:
        collected_colors = add_to_colors(collected_colors, secondary_colors, word_first, word_second)
    else:
        text.insert(len(text) // 2, first_part[:-1])
        text.insert(len(text) // 2, second_part[:-1])
        text = deque([x for x in text if x != ""])

if text:
    if text[0] in main_colors or text[0] in secondary_colors:
        collected_colors.append(text[0])

final_colors = []
for color in collected_colors:
    if color in main_colors:
        final_colors.append(color)
    elif color in secondary_colors:
        if secondary_colors[color][0] in collected_colors and secondary_colors[color][1] in collected_colors:
            final_colors.append(color)
print(final_colors)
