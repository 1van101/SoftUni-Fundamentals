from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    food_types = {
        "Bread": Bread,
        "Cake": Cake
    }
    drink_types = {
        "Tea": Tea,
        "Water": Water
    }
    table_types = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    def __check_if_food_exists(self, name):
        for food in self.food_menu:
            if food.name == name:
                return food

    def __check_if_drink_exists(self, name):
        for drink in self.drinks_menu:
            if drink.name == name:
                return drink

    def __check_if_table_exists(self, number):
        for table in self.tables_repository:
            if table.table_number == number:
                return table

    def add_food(self, food_type, name, price):
        food = self.__check_if_food_exists(name)

        if food:
            raise Exception(f"{food_type} {name} is already in the menu!")

        new_food = self.food_types[food_type](name, price)
        self.food_menu.append(new_food)

        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        drink = self.__check_if_drink_exists(name)

        if drink:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        new_drink = self.drink_types[drink_type](name, portion, brand)
        self.drinks_menu.append(new_drink)

        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, number, capacity):
        if self.__check_if_table_exists(number):
            raise Exception(f"Table {number} is already in the bakery!")

        new_table = self.table_types[table_type](number, capacity)
        self.tables_repository.append(new_table)

        return f"Added table number {number} in the bakery"

    def reserve_table(self, number_of_people):
        suitable_tables = [x for x in self.tables_repository if not x.is_reserved and x.capacity >= number_of_people]

        if not suitable_tables:
            return f"No available table for {number_of_people} people"

        table = suitable_tables[0]
        table.reserve(number_of_people)

        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number, *args):
        table = self.__check_if_table_exists(table_number)
        if not table:
            return f"Could not find table {table_number}"

        ordered_foods = []
        foods_not_in_menu = []

        for food_name in args:
            food = self.__check_if_food_exists(food_name)
            if not food:
                foods_not_in_menu.append(food_name)
                continue

            table.order_food(food)
            ordered_foods.append(food)

        output = [f"Table {table_number} ordered:"]
        output.extend(repr(x) for x in ordered_foods)

        output.append(f"{self.__name} does not have in the menu:")
        output.extend(x for x in foods_not_in_menu)

        return "\n".join(output)

    def order_drink(self, table_number, *args):
        table = self.__check_if_table_exists(table_number)
        if not table:
            return f"Could not find table {table_number}"

        ordered_drinks = []
        drinks_not_in_menu = []

        for drink_name in args:
            drink = self.__check_if_drink_exists(drink_name)
            if not drink:
                drinks_not_in_menu.append(drink_name)
                continue

            table.order_drink(drink)
            ordered_drinks.append(drink)

        output = [f"Table {table_number} ordered:"]
        output.extend(repr(x) for x in ordered_drinks)

        output.append(f"{self.__name} does not have in the menu:")
        output.extend(x for x in drinks_not_in_menu)

        return "\n".join(output)

    def leave_table(self, table_number):
        table = self.__check_if_table_exists(table_number)
        if table:
            self.total_income += table.get_bill()
            table_bill = table.get_bill()
            table.clear()

            return f"Table: {table_number}\nBill: {table_bill:.2f}"

    def get_free_tables_info(self):
        return "\n".join(t.free_table_info() for t in self.tables_repository)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"


