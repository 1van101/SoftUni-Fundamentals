card_deck = input().split()
number_shuffles = int(input())
middle_deck = len(card_deck) // 2

for shuffle in range(number_shuffles):
    left_half = card_deck[:middle_deck]
    right_half = card_deck[middle_deck:]
    card_deck.clear()
    for card in range(len(left_half)):
        card_deck.append(left_half[card])
        card_deck.append((right_half[card]))

print(card_deck)