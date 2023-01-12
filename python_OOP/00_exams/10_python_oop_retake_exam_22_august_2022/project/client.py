class Client:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0
        self.ordered_meals = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not all([
            len(value) == 10,
            value[0] == "0",
            value.isnumeric()
        ]):
            raise ValueError("Invalid phone number!")

        self.__phone_number = value
