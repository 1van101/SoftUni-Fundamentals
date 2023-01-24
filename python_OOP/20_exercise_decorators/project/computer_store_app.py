from computer_types.computer import Computer
from computer_types.desktop_computer import DesktopComputer
from computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    @staticmethod
    def _computer_price_validation(comp_price, client_budget):
        return comp_price <= client_budget

    @staticmethod
    def _processor_validation(requested_processor, actual_processor):
        return requested_processor == actual_processor

    @staticmethod
    def _ram_validation(requested_ram, actual_ram):
        return actual_ram >= requested_ram

    def build_computer(self, type_computer, manufacturer, model, processor, ram):
        if type_computer not in ["Laptop", "Desktop Computer"]:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        if type_computer == "Laptop":
            new_laptop = Laptop(manufacturer, model)

        elif type_computer == "Desktop Computer":
            new_laptop = DesktopComputer(manufacturer, model)

        configured_laptop = new_laptop.configure_computer(processor, ram)
        self.warehouse.append(new_laptop)

        return configured_laptop

    def sell_computer(self, budget, wanted_processor, wanted_ram):
        searched_computer = None
        for computer in self.warehouse:
            if all([
                self._processor_validation(wanted_processor, computer.processor),
                self._ram_validation(wanted_ram, computer.ram),
                self._computer_price_validation(computer.price, budget)
            ]):
                searched_computer = computer
        if not searched_computer:
            raise Exception("Sorry, we don't have a computer for you.")

        profit = budget - searched_computer.price
        self.profits += profit
        self.warehouse.remove(searched_computer)
        return f"{searched_computer} sold for {budget}$."
