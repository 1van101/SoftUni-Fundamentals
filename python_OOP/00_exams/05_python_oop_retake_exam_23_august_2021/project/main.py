from project_for_movies.astronaut.astronaut import Astronaut
from project_for_movies.astronaut.biologist import Biologist
from project_for_movies.astronaut.geodesist import Geodesist
from project_for_movies.planet.planet import Planet
from project_for_movies.space_station import SpaceStation

s = SpaceStation()
# p = Planet("asd")
print(s.add_astronaut("Biologist", "Ivan"))
print(s.add_astronaut("Meteorologist", "Stoyan"))
# print(s.add_astronaut("Meteorologist", "Stoyan"))
print(s.add_astronaut("Biologist", "Petar"))
print(s.add_astronaut("Biologist", "Kosio"))
print(s.add_astronaut("Geodesist", "Koko"))
# print(s.add_astronaut("Geodesist", "Koko"))
# print(s.add_planet("Pluton", "1, 2, 3"))
print(s.add_planet("Pluton", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23"))
# print(s.add_planet("Pluton", "1, 2, 3"))
# print(s.retire_astronaut("Ivan"))
print(s.send_on_mission("Pluton"))
print(s.report())