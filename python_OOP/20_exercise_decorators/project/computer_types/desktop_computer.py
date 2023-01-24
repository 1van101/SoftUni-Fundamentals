from computer_types.computer import Computer
from computer_types.valid_ram_sizes import valid_ram_sizes
from math import log


class DesktopComputer(Computer):
    ALLOWED_PROCESSORS = {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800
    }
    MAXIMUM_RAM_ALLOWED = 128

    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor, ram):
        if processor not in self.ALLOWED_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if ram > self.MAXIMUM_RAM_ALLOWED or ram not in valid_ram_sizes(self.MAXIMUM_RAM_ALLOWED):
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        price = log(ram, 2) * 100 + self.ALLOWED_PROCESSORS[processor]
        self.price = price
        self.processor = processor
        self.ram = ram

        return f"Created {self.manufacturer} {self.model} with " \
               f"{processor} and {ram}GB RAM for {int(price)}$."
