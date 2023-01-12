class Controller:
    VALID_SUPPLIES = {"Food": "food", "Drink": "drink"}

    def __init__(self):
        self.players = []
        self.supplies = []

    def __get_player(self, name):
        for p in self.players:
            if p.name == name:
                return p

    def __get_supplies_by_type_if_exist(self, sustenance_type):
        supplies = [x for x in self.supplies if type(x).__name__ == sustenance_type]
        if not supplies:
            raise Exception(f"There are no {self.VALID_SUPPLIES[sustenance_type]} supplies left!")

        return supplies

    @staticmethod
    def __duel(attacker, defender):
        defender.stamina -= attacker.stamina * 0.5

        if defender.stamina * 0.5 >= attacker.stamina:
            attacker.stamina = 0
        else:
            attacker.stamina -= defender.stamina * 0.5

        if attacker.stamina > defender.stamina:
            return f"Winner: {attacker.name}"

        return f"Winner: {defender.name}"

    @staticmethod
    def __can_not_duel(player1, player2):
        output = []
        if player1.stamina == 0:
            output.append(f"Player {player1.name} does not have enough stamina.")
        if player2.stamina == 0:
            output.append(f"Player {player2.name} does not have enough stamina.")

        if output:
            return "\n".join(output)

    def add_player(self, *args):
        successfully_added_players = []

        for player in args:
            if player not in self.players:
                self.players.append(player)
                successfully_added_players.append(player)

        return f"Successfully added: {', '.join(x.name for x in successfully_added_players)}"

    def add_supply(self, *args):
        self.supplies.extend(args)

    def sustain(self, player_name, sustenance_type):
        player = self.__get_player(player_name)

        if not player or sustenance_type not in self.VALID_SUPPLIES:
            return

        supplies_by_type = self.__get_supplies_by_type_if_exist(sustenance_type)
        current_supply = supplies_by_type.pop()

        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        if player.stamina + current_supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += current_supply.energy

        for i in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[i].name == current_supply.name:
                self.supplies.pop(i)
                break

        return f"{player_name} sustained successfully with {current_supply.name}."

    def duel(self, first_player_name, second_player_name):
        first_player = self.__get_player(first_player_name)
        second_player = self.__get_player(second_player_name)

        if self.__can_not_duel(first_player, second_player):
            return self.__can_not_duel(first_player, second_player)

        attacker = first_player if first_player.stamina < second_player.stamina else second_player
        defender = first_player if first_player.stamina > second_player.stamina else second_player

        return self.__duel(attacker, defender)

    def next_day(self):
        for player in self.players:
            if player.stamina - player.age * 2 < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

        for player in self.players:
            for supply in self.VALID_SUPPLIES:
                self.sustain(player.name, supply)

    def __str__(self):
        output = []

        for player in self.players:
            output.append(str(player))

        for supply in self.supplies:
            output.append(supply.details())

        return '\n'.join(output)
