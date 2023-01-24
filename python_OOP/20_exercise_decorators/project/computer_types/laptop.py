from computer_types.computer import Computer
from computer_types.valid_ram_sizes import valid_ram_sizes
from math import log


class Laptop(Computer):
    ALLOWED_PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200
    }
    MAXIMUM_RAM_ALLOWED = 64

    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor, ram):
        if processor not in self.ALLOWED_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        if ram > self.MAXIMUM_RAM_ALLOWED or ram not in valid_ram_sizes(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        price = log(ram, 2) * 100 + self.ALLOWED_PROCESSORS[processor]
        self.price = price
        self.processor = processor
        self.ram = ram

        return f"Created {self.manufacturer} {self.model} with " \
               f"{processor} and {ram}GB RAM for {int(price)}$."
