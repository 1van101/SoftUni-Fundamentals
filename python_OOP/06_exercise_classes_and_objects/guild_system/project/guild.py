from player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild == player.DEFAULT_GUILD:
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name):
        try:
            player_to_be_kicked = [x for x in self.players if x.name == player_name][0]
            self.players.remove(player_to_be_kicked)
            player_to_be_kicked.guild = Player.DEFAULT_GUILD
            return f"Player {player_name} has been removed from the guild."
        except IndexError:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players_info = '\n'.join([x.player_info() for x in self.players])
        return f"Guild: {self.name}\n{players_info}"


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
