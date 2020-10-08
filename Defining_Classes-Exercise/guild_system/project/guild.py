from guild_system.project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.a_list_of_players = []

    def assign_player(self, player):
        if player in self.a_list_of_players:
            return f"Player {player.name} is already in the guild."
        elif player.guild == 'Unaffiliated':
            self.a_list_of_players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        player_to_kick = [player for player in self.a_list_of_players if player.name == player_name]
        if len(player_to_kick) == 0:
            return f"Player {player_name} is not in the guild."
        self.a_list_of_players.remove(player_to_kick[0])
        player_to_kick[0].guild = 'Unaffiliated'
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        info = f"Guild: {self.name}\n"
        for player in self.a_list_of_players:
            info += player.player_info()
        return info


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
print(guild.kick_player('Pesho'))

