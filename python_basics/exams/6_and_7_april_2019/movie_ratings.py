import sys

movies = int(input())
highest_rating = -sys.maxsize
lowest_rating = sys.maxsize
highest_rating_movie = ""
lowest_rating_movie = ""
rating_counter = 0

for movie in range(movies):
    name = input()
    rating = float(input())
    rating_counter += rating
    if rating >highest_rating:
        highest_rating = rating
        highest_rating_movie = name
    if rating < lowest_rating:
        lowest_rating = rating
        lowest_rating_movie = name
print(f"{highest_rating_movie} is with highest rating: {highest_rating}")
print(f"{lowest_rating_movie} is with lowest rating: {lowest_rating}")
print(f"Average rating: {rating_counter / movies:.1f}")
