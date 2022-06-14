electrons = int(input())
shell_of_electrons = []
shell = 1

while electrons > 0:
    if electrons - 2 * (shell ** 2) < 0:
        shell_of_electrons.append(electrons)
    else:
        shell_of_electrons.append(2 * (shell ** 2))
    electrons -= 2 * (shell ** 2)
    shell += 1

print(shell_of_electrons)