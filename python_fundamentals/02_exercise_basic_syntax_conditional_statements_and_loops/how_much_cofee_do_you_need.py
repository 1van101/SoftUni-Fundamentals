events = ["coding", "dog", "cat", "movie"]
coffees = 0
extra_sleep_needed = False
while True:
    command = input()
    if command == "END":
        break
    if command.isupper():
        if command.lower() in events:
            coffees += 2
    else:
        if command in events:
            coffees += 1
    if coffees > 5:
        extra_sleep_needed = True
        break

if extra_sleep_needed:
    print("You need extra sleep")
else:
    print(coffees)