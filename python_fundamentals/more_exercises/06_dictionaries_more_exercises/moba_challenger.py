def player_existence(dct, name):
    if name in dct:
        return True
    return False


def add_position_to_player(dct_players, total_points, name, position, skill):
    if not player_existence(dct_players, name):
        dct_players[name] = {position: skill}
        total_points[name] = skill
    else:
        if position in dct_players[name]:
            if dct_players[name][position] < skill:
                dct_players[name][position] = skill
                diff = dct_players[name][position] - skill
                total_points[name] += diff
        else:
            dct_players[name][position] = skill
            total_points[name] += skill
    return dct_players, total_points


def battle(dct_players, total_points, player1, player2):
    common_position = False
    if player_existence(dct_players, player1) and player_existence(dct_players, player2):
        for position in dct_players[player1]:
            if position in dct_players[player2]:
                common_position = True
                break
        if common_position:
            if total_points[player1] > total_points[player2]:
                del dct_players[player2]
                del total_points[player2]
            elif total_points[player2] > total_points[player1]:
                del dct_players[player1]
                del total_points[player1]
    return dct_players, total_points


moba_players = {}
total_skill_points = {}
command = input()
while not command == "Season end":
    if " -> " in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        moba_players, total_skill_points = add_position_to_player(moba_players, total_skill_points, player, position,
                                                                  skill)
    elif " vs " in command:
        first_player, second_player = command.split(" vs ")
        moba_players, total_skill_points = battle(moba_players, total_skill_points, first_player, second_player)
    command = input()

total_skill_points_sorted = dict(sorted(total_skill_points.items(), key=lambda kv: (-kv[1], kv[0])))

for name, number in total_skill_points_sorted.items():
    print(f"{name}: {number} skill")
    [print(f"- {x} <::> {y}") for x, y in sorted(moba_players[name].items(), key=lambda kv: (-kv[1], kv[0]))]
