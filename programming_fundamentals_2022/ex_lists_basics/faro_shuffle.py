deck_of_cards = input().split()
count_shuffles = int(input())
for shuffle in range(count_shuffles):
    mixed_cards = []
    middle_of_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_of_deck]
    right_part = deck_of_cards[middle_of_deck:]
    for index_of_card in range(len(left_part)):
        mixed_cards.append(left_part[index_of_card])
        mixed_cards.append(right_part[index_of_card])
        deck_of_cards = mixed_cards
print(deck_of_cards)