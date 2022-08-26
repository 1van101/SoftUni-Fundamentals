hat_trick = False
many_gols = False
best_player = ""
gols_of_the_player = 0
while True:
    player = input()
    if player == "END":
        break
    gols = int(input())
    if gols > gols_of_the_player:
        gols_of_the_player = gols
        best_player = player
    if gols >= 3:
        hat_trick = True
        break
    elif gols >= 10:
        many_gols = True
        break
print(f"{player} is the best player!")
if hat_trick or many_gols:
    print(f"He has scored {gols_of_the_player} goals and made a hat-trick !!!")
else:
    print(f"He has scored {gols_of_the_player} goals.")
