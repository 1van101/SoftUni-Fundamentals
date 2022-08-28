import math

easter_bread = int(input())
sugar_used = 0
flour_used = 0
max_sugar_used = 0
max_flour_used = 0
for e_b in range(easter_bread):
    sugar = int(input())
    flour = int(input())
    sugar_used += sugar
    flour_used += flour
    if sugar > max_sugar_used:
        max_sugar_used = sugar
    if flour > max_flour_used:
        max_flour_used = flour
sugar_packages = math.ceil(sugar_used / 950)
flour_packages = math.ceil(flour_used / 750)

print(f"Sugar: {sugar_packages}")
print(f"Flour: {flour_packages}")
print(f"Max used flour is {max_flour_used} grams, "
      f"max used sugar is {max_sugar_used} grams.")


