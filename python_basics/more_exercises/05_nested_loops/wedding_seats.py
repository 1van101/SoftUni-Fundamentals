max_sector = input()
rows_number = int(input())
odd_seats_number = int(input())
min_sector = "A"
total_seats = 0
def char_range(char_start, char_end):
    for char in range(ord(char_start), ord(char_end) + 1):
        yield chr(char)
for sector in char_range(min_sector, max_sector):
    for rows in range(1, rows_number + 1):
        if rows % 2 != 0:
            for odd in range(1, odd_seats_number + 1):
                odd = chr(odd + 96)
                total_seats += 1
                print(f"{sector}{rows}{odd}")
        elif rows % 2 == 0:
            for even in range(1, odd_seats_number + 3):
                even = chr(even + 96)
                total_seats += 1
                print(f"{sector}{rows}{even}")
    rows_number += 1
print(total_seats)

# max_sector = input()
# rows_in_first_sector = int(input())
# seats_in_odd_row = int(input())
# counter = 0
# for sector in range(ord("A"), ord(max_sector)+1):
#     for rows in range(1, rows_in_first_sector + 1):
#         if rows % 2 != 0:
#             for seats in range(97, seats_in_odd_row + 97):
#                 print(f"{chr(sector)}{rows}{chr(seats)}")
#                 counter += 1
#         else:
#             for seats in range(97,seats_in_odd_row + 99):
#                 print(f"{chr(sector)}{rows}{chr(seats)}")
#                 counter += 1
#     rows_in_first_sector += 1
# print(counter)

