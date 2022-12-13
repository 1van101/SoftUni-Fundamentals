def math_operations(*args, **kwargs):
    result = ""

    for i in range(len(args)):
        position = i % len(kwargs)
        if position == 0:
            kwargs["a"] += args[i]
        elif position == 1:
            kwargs["s"] -= args[i]
        elif position == 2:
            try:
                kwargs["d"] /= args[i]
            except ZeroDivisionError:
                continue
        elif position == 3:
            kwargs["m"] *= args[i]

    for letter, res in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
        result += f"{letter}: {res:.1f}" + "\n"
    return result


print(math_operations(6.0, a=0, s=0, d=5, m=0))
