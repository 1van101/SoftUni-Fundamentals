import re

text = input()

match = re.findall(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b', text)
print(" ".join(match))