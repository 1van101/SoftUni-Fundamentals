command = input()
limit_is_reached = False
points = 0
the_best_movie = ""
movie_counter = 0

while command != "STOP":
    movie_counter += 1
    current_points = 0
    if movie_counter == 7:
        limit_is_reached = True
        break
    command_len = len(command)
    for char, symbol in enumerate(command):
        current_points += ord(symbol)
        if symbol.isupper():
            current_points -= command_len
        elif symbol.islower():
            current_points = current_points - (2 * command_len)
    if current_points > points:
        points = current_points
        the_best_movie = command

    command = input()

if limit_is_reached:
    print("The limit is reached.")
print(f"The best movie for you is {the_best_movie} with {points} ASCII sum.")

# limit_is_reached = True
# max_points = 0
# the_best_movie = ""
# for movie in range(7):
#     current_points = 0
#     current_movie = input()
#     if current_movie == "STOP":
#         limit_is_reached = False
#         break
#     for chars in current_movie:
#         current_points += ord(chars)
#         if chars.islower():
#             current_points -= 2 * len(current_movie)
#         elif chars.isupper():
#             current_points -= len(current_movie)
#
#     if current_points > max_points:
#         max_points = current_points
#         the_best_movie = current_movie
#
# if limit_is_reached:
#     print("The limit is reached.")
# print(f"The best movie for you is {the_best_movie} with {max_points} ASCII sum.")


