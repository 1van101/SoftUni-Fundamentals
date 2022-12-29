from math import log


def get_log(n, base):
    if base.isdigit():
        return log(n, int(base))
    return log(n)


number = int(input())
base = input()

print(f"{get_log(number, base):.2f}")