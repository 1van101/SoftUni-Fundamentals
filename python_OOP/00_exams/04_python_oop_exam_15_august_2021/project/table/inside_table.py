from project.table.table import Table


class InsideTable(Table):
    min_table_number = 1
    max_table_number = 50

    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value < self.min_table_number or value > self.max_table_number:
            raise ValueError(
                f"Inside table's number must be between {self.min_table_number} and {self.max_table_number} inclusive!")

        self.__table_number = value
