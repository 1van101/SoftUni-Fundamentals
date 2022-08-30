first_player_eggs = int(input())
second_player_eggs = int(input())
battle_is_over = False
while True:
    command = input()
    if command == "End of battle":
        battle_is_over = True
        break
    if command == "one":
        second_player_eggs -= 1
    else:
        first_player_eggs -= 1
    if first_player_eggs <= 0:
        print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
        break
    if second_player_eggs <= 0:
        print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
        break

if battle_is_over:
    print(f"Player one has {first_player_eggs} eggs left.")
    print(f"Player two has {second_player_eggs} eggs left.")