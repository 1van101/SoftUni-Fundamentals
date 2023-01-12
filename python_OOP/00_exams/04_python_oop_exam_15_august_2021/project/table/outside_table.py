from project.table.table import Table


class OutsideTable(Table):
    min_table_number = 51
    max_table_number = 100

    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value < self.min_table_number or value > self.max_table_number:
            raise ValueError(
                f"Outside table's number must be between {self.min_table_number} and {self.max_table_number} inclusive!")

        self.__table_number = value