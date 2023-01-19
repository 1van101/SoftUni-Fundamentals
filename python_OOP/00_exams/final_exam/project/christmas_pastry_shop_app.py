from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    valid_delicacies = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen
    }
    valid_booths = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth
    }

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def __check_if_delicacy_exists(self, name):
        for delicacy in self.delicacies:
            if delicacy.name == name:
                return delicacy

    def __check_if_booth_exists_by_number(self, number):
        for booth in self.booths:
            if booth.booth_number == number:
                return booth

    def add_delicacy(self, type_delicacy, name, price):
        delicacy = self.__check_if_delicacy_exists(name)

        if delicacy:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.valid_delicacies:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = self.valid_delicacies[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth, booth_number, capacity):
        booth = self.__check_if_booth_exists_by_number(booth_number)

        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.valid_booths:
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = self.valid_booths[type_booth](booth_number, capacity)
        self.booths.append(new_booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people):
        suitable_booths = [x for x in self.booths if not x.is_reserved and x.capacity >= number_of_people]

        if not suitable_booths:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth = suitable_booths[0]
        booth.reserve(number_of_people)

        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number, delicacy_name):
        booth = self.__check_if_booth_exists_by_number(booth_number)

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self.__check_if_delicacy_exists(delicacy_name)

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number):
        booth = self.__check_if_booth_exists_by_number(booth_number)

        price_for_all_orders = sum([x.price for x in booth.delicacy_orders])
        bill = booth.price_for_reservation + price_for_all_orders

        self.income += bill

        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

