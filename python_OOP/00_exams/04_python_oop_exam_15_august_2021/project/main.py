from project.bakery import Bakery
from project.table.outside_table import OutsideTable

bakery = Bakery("Name")

print(bakery.add_table("InsideTable", 5, 5))
# print(bakery.add_table("OutsideTable", 5, 5))
print(bakery.add_drink("Tea", "Earl Grey", 200, "black"))
# print(bakery.add_drink("Water", "Earl Grey", 200, "black"))
print(bakery.add_drink("Water", "Devin", 500, "devin"))
print(bakery.add_food("Bread", "Banana", 3.4))
print(bakery.add_food("Cake", "Carrot Cake", 2.4))
print(bakery.add_table("OutsideTable", 61, 8))
# print(bakery.reserve_table(7))
print(bakery.order_food(61, "Makaroni", "Banana", "Carrot Cake", "Pasta"))
# print(bakery.order_drink(61, "Devin", "Earl Grey", "Beer", "Wine"))
# print(bakery.leave_table(61))
print(bakery.get_free_tables_info())
print(bakery.get_total_income())