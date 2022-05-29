n = int(input())

list_of_shells = []
counter = 1
while True:
    electrons_in_shell = 2 * (counter ** 2)
    n -= electrons_in_shell
    if n <= 0:
        list_of_shells.append(electrons_in_shell - abs(n))
        break
    else:
        list_of_shells.append(electrons_in_shell)
    counter += 1

print(list_of_shells)
