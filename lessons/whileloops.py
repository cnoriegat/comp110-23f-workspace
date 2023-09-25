"""Demonstrate while loops by finding low value in string"""

cards: str = "5235"
idx: int = 0
low_card: int = int(cards[0])

#look at each number in the string
while idx < len(cards):
    current_card: int = int(cards[idx])
    if current_card < low_card:
        low_card = current_card
    idx += 1

print(low_card)