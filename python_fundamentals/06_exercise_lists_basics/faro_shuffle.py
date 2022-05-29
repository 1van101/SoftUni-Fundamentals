card_deck = input().split()
shuffle = int(input())
shuffled_deck = []
for i in range(shuffle):
    shuffled_deck = []
    card_deck_separated = len(card_deck) // 2
    left_half = card_deck[:card_deck_separated]
    right_half = card_deck[card_deck_separated:]
    for j in range(card_deck_separated):
        shuffled_deck.append(left_half[j])
        shuffled_deck.append(right_half[j])
    card_deck = shuffled_deck
print(shuffled_deck)