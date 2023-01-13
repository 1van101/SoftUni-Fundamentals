from project import Player

class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name):
        player_to_remove = [x for x in self.__players if x.name == player_name]
        try:
            self.__players.remove(player_to_remove[0])
            return player_to_remove[0]
        except IndexError:
            return f"Player {player_name} not found"