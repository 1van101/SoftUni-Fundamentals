tickets_counter = 0
students_counter = 0
standard_counter = 0
kids_counter = 0
while True:
    command = input()
    if command == "Finish":
        break
    tickets_num = int(input())

    current_tickets_counter = 0
    current_command = command
    valid = False

    for places in range(tickets_num):
        ticket_type = input()
        if ticket_type == "End":
            valid = True
            break
        current_tickets_counter += 1
        tickets_counter += 1

        if ticket_type == "student":
            students_counter += 1
        elif ticket_type == "standard":
            standard_counter += 1
        elif ticket_type == "kid":
            kids_counter += 1

        if current_tickets_counter == tickets_num:
            valid = True
            break



    if valid:
        print(f"{current_command} - {current_tickets_counter / tickets_num * 100:.2f}% full.")
print(f"Total tickets: {tickets_counter}")
print(f"{students_counter / tickets_counter * 100:.2f}% student tickets.")
print(f"{standard_counter / tickets_counter * 100:.2f}% standard tickets.")
print(f"{kids_counter / tickets_counter * 100:.2f}% kids tickets.")