"""Practicing Counters"""

num_string: str = "123"

num_string_int: int(num_string)

num_of_odds: int = 0

while int(num_string[0]) % 2 == 1:
    odd_cards: num_string[num_of_odds]
    num_of_odds = num_of_odds + 1

print(odd_cards)