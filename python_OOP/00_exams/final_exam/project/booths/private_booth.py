from project.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_PER_PERSON = 3.50

    def __init__(self, booth_number, capacity):
        super().__init__(booth_number, capacity)

