one_lev_coins = int(input())
two_leva_coins = int(input())
five_leva_banknotes = int(input())
sum = int(input())

for n1 in range(0, one_lev_coins + 1):
    for n2 in range(0, two_leva_coins + 1):
        for n3 in range(0, five_leva_banknotes + 1):
            if n1 + (2 * n2) + (5 * n3) == sum:
                print(f"{n1} * 1 lv. + {n2} * 2 lv. + {n3} * 5 lv. = {sum} lv.")