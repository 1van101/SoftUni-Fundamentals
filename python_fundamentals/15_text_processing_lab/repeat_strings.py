words = input().split()
repeated_words = [x * len(x) for x in words]
print("".join(repeated_words))