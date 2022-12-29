def create(length):
    fibonacci_sequence = [0, 1]
    for _ in range(2, length):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    print(*fibonacci_sequence)
    return fibonacci_sequence


def locate(n, fib_seq):
    try:
        print(f"The number - {n} is at index {fib_seq.index(n)}")
    except ValueError:
        print(f"The number {n} is not in the sequence")