from .fibonacci_seq import *


def do_the_commands():
    fibonacci_sequence = []
    while True:
        command = input().split()
        action = command[0]
        if action == "Stop":
            break
        if action == "Create":
            fibonacci_sequence = create(int(command[2]))
        elif action == "Locate":
            locate(int(command[1]), fibonacci_sequence)