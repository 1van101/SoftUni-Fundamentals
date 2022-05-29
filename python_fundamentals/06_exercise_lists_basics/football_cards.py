players_sent_off = input()

team_a_counter = 11
team_b_counter = 11
list_red_cards = players_sent_off.split(" ")
is_terminated = False
list_red_cards = set(list_red_cards)
for players in list_red_cards:
    team_letter = players[0]
    if team_letter == "A":
        team_a_counter -= 1
    elif team_letter == "B":
        team_b_counter -= 1
    if team_a_counter < 7 or team_b_counter < 7:
        is_terminated = True
        break
print(f"Team A - {team_a_counter}; Team B - {team_b_counter}")
if is_terminated:
    print("Game was terminated")