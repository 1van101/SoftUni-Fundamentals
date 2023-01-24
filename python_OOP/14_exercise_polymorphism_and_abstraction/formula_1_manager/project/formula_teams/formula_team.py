from abc import ABC, abstractmethod


class FormulaTeam(ABC):

    def __init__(self, budget):
        self.budget = budget

    @property
    @abstractmethod
    def SPONSORS(self):
        pass

    @property
    @abstractmethod
    def EXPENSES(self):
        pass


    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    def calculate_revenue_after_race(self, position):
        revenue = - self.EXPENSES
        for tuple in self.SPONSORS.values():
            for place, award in tuple.items():
                if position <= place:
                    revenue += award
                    break

        self.__budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.__budget}$"
