from project.client import Client


class FoodOrdersApp:
    ALLOWED_MEALS = ["Starter", "MainDish", "Dessert"]
    receipt_id = 1

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def __check_if_client_exist(self, phone_number):
        client = [x for x in self.clients_list if x.phone_number == phone_number]
        if client:
            return client[0]

    def __check_if_meal_in_menu(self, meal_name):
        if any([x.name == meal_name for x in self.menu]):
            return True

    def register_client(self, client_phone_number):
        if self.__check_if_client_exist(client_phone_number):
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if type(meal).__name__ in self.ALLOWED_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        output = [x.details() for x in self.menu]
        return '\n'.join(output)

    def add_meals_to_shopping_cart(self, client_phone_number, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = self.__check_if_client_exist(client_phone_number)
        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        current_order = {}

        for meal_name, qty in meal_names_and_quantities.items():
            if not self.__check_if_meal_in_menu(meal_name):
                raise Exception(f"{meal_name} is not on the menu!")

            current_meal = [x for x in self.menu if x.name == meal_name][0]

            if qty > current_meal.quantity:
                raise Exception(f"Not enough quantity of {type(current_meal).__name__}: {meal_name}!")

            current_order[meal_name] = qty

        # client.shopping_cart.extend(current_order)
        for meal_name, qty in current_order.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    client.shopping_cart.append(meal)
                    # if meal_name not in client.ordered_meals:
                    #     client.ordered_meals[meal_name] = 0
                    client.ordered_meals[meal_name] = qty
                    client.bill += qty * meal.price
            # client.bill += current_meal.price * qty

        for meal_name, qty in client.ordered_meals.items():
            for meal in self.menu:
                if meal_name == meal.name:
                    meal.quantity -= qty
                    # client.bill += qty * meal.price

        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join(x.name for x in client.shopping_cart)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number):
        client = self.__check_if_client_exist(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            for meal_name, qty in client.ordered_meals.items():
                if meal.name == meal_name:
                    meal.quantity += qty

        client.shopping_cart = []
        client.ordered_meals = {}
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        client = self.__check_if_client_exist(client_phone_number)

        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        client_bill = client.bill
        client.bill = 0
        client.shopping_cart = []
        client.ordered_meals = {}
        current_receipt = self.receipt_id
        self.receipt_id += 1

        return f"Receipt #{current_receipt} with total amount of {client_bill:.2f} was successfully paid for {client.phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
