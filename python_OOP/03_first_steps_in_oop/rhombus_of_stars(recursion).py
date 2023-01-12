def print_rhombus(n, i=1):
    star_pattern = ("* " * i).rstrip()
    if i == n:
        print(star_pattern)
        return
    print(" " * (n - i - 1), star_pattern)
    print_rhombus(n, i + 1)
    print(" " * (n - i - 1), star_pattern)


n = int(input())
print_rhombus(n)
