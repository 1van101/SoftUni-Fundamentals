class Party:
    def __init__(self):
        self.people_list = []

    def get_info(self):
        people_result = ", ".join(self.people_list)
        return f"Going: {people_result}\nTotal: {len(self.people_list)}"


party = Party()
while True:
    person_input = input()
    if person_input == "End":
        break
    party.people_list.append(person_input)

print(party.get_info())




