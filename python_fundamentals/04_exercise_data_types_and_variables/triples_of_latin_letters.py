num = int(input())
for first_let in range(97, num + 97):
    for second_let in range(97, num + 97):
        for third_let in range(97, num + 97):
            print(f"{chr(first_let)}{chr(second_let)}{chr(third_let)}")
