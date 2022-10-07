party = set()

number_of_guests = int(input())
for _ in range(number_of_guests):
    party.add(input())

guest = input()
while not guest == "END":
    party.discard(guest)
    guest = input()

print(len(party))
[print(x) for x in sorted(party)]