from formula_teams.formula_team import FormulaTeam
from formula_teams.red_bull_sponsors import RED_BULL_SPONSORS


class RedBullTeam(FormulaTeam):
    # SPONSORS = RED_BULL_SPONSORS
    # EXPENSES = 250_000
    def __init__(self, budget):
        super().__init__(budget)

    @property
    def SPONSORS(self):
        return RED_BULL_SPONSORS

    @property
    def EXPENSES(self):
        return 250_000
