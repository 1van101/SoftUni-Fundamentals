first_player_name = input()
second_player_name = input()
first_player_points = 0
second_player_points = 0
end_of_game = False
number_wars_first_player = False
number_wars_second_player = False

while True:
    command = input()
    if command == "End of game":
        end_of_game = True
        break
    first_player_card = int(command)
    second_player_card = int(input())
    diff = abs(first_player_card - second_player_card)
    if first_player_card > second_player_card:
        first_player_points += diff
    elif first_player_card < second_player_card:
        second_player_points += diff
    else:
        another_card_first_player = int(input())
        another_card_second_player = int(input())
        if another_card_first_player > another_card_second_player:
            number_wars_first_player = True
            break
        else:
            number_wars_second_player = True
            break
if end_of_game:
    print(f"{first_player_name} has {first_player_points} points")
    print(f"{second_player_name} has {second_player_points} points")
if number_wars_first_player:
    print(f"Number wars!")
    print(f"{first_player_name} is winner with {first_player_points} points")
elif number_wars_second_player:
    print(f"Number wars!")
    print(f"{second_player_name} is winner with {second_player_points} points")

