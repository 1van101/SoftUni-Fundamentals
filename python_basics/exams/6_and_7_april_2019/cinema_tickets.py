students_counter = 0
standard_counter = 0
kids_counter = 0
total_tickets_counter = 0

while True:
    movie_starts = False
    current_movie_tickets_counter = 0
    command = input()
    if command == "Finish":
        break
    free_seats = int(input())
    for seats in range(1, free_seats + 1):
        type_of_ticket = input()
        if type_of_ticket == "End":
            movie_starts = True
            break
        current_movie_tickets_counter += 1
        if type_of_ticket == "student":
            students_counter += 1
        elif type_of_ticket == "standard":
            standard_counter += 1
        else:
            kids_counter += 1
        total_tickets_counter += 1
        if seats == free_seats:
            movie_starts = True
    if movie_starts:
        print(f"{command} - {current_movie_tickets_counter / free_seats * 100:.2f}% full.")

print(f"Total tickets: {total_tickets_counter}")
print(f"{students_counter / total_tickets_counter * 100:.2f}% student tickets.")
print(f"{standard_counter / total_tickets_counter * 100:.2f}% standard tickets.")
print(f"{kids_counter / total_tickets_counter * 100:.2f}% kids tickets.")