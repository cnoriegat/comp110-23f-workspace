"""Practicing counters."""

cards: str = "123456789"
num_odds: int = 0
idx: int = 0

while idx < len(cards):
    if int(cards[idx]) % 2 == 1:
        num_odds += 1
    idx += 1

print(num_odds)