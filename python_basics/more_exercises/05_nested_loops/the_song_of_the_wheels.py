value = int(input())
counter = 0
password = ""

password_is_found = False
for a in range (1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a * b + c * d == value and a < b and c > d:
                    counter += 1
                    if counter == 4:
                        password_is_found = True
                        password = str(a) + str(b) + str(c) + str(d)
                    print(f"{a}{b}{c}{d}", end =" ")

if password_is_found:
    print()
    print(f"Password: {password}")
else:
    if counter == 0:
        print("No!")
    else:
        print()
        print("No!")

