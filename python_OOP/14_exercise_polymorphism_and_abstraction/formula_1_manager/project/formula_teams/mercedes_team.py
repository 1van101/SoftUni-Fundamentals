from formula_teams.formula_team import FormulaTeam
from formula_teams.mercedes_sponsors import MERCEDES_SPONSORS


class MercedesTeam(FormulaTeam):
    # SPONSORS = MERCEDES_SPONSORS
    # EXPENSES = 200_000
    def __init__(self, budget):
        super().__init__(budget)

    @property
    def SPONSORS(self):
        return MERCEDES_SPONSORS

    @property
    def EXPENSES(self):
        return 200_000
