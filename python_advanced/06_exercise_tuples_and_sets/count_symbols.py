text = input()
occurrences = {x: text.count(x) for x in text}
[print(f"{x}: {y} time/s") for x, y in sorted(occurrences.items())]