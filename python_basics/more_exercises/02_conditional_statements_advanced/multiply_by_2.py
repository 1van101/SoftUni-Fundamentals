import sys

for i in range(0, sys.maxsize):
    num = float(input())
    result = num * 2
    if num < 0:
        print("Negative number!")
        break
    else:
        print(f"Result: {result:.2f} ")
