"""
Dobble game is comparing two sets and finding the comon object
"""

import string
import random


symbols = list(string.ascii_letters)
card_one = [0] * 5
card_two = [0] * 5
# pos_one and pos_two are same symbol positions in both cards
pos_one = random.randint(0, 4)
pos_two = random.randint(0, 4)

same_symbol = random.choice(symbols)
symbols.remove(same_symbol)  # Remove same_symbol to avoid replication

if pos_one == pos_two:
    # Assign the same symbol to same position
    card_one[pos_one] = same_symbol
    card_two[pos_one] = same_symbol

else:
    # Assign same symbol to respective index positions
    card_one[pos_one] = same_symbol
    card_two[pos_two] = same_symbol

    """
    Assign elements to swapped positions of lists.
    Otherwise those indices won't be replaced
    """
    card_one[pos_two] = random.choice(symbols)
    symbols.remove(card_one[pos_two])
    card_two[pos_one] = random.choice(symbols)
    symbols.remove(card_two[pos_one])

i = 0
while i < 5:
    if i != pos_one and i != pos_two:
        """
        Condition satisfies when value of 'i' is neither pos_one nor pos_two
        If satisfied, assign two different characters at i'th index of poth cards
        """
        alphabet_one = random.choice(symbols)
        symbols.remove(alphabet_one)
        alphabet_two = random.choice(symbols)
        symbols.remove(alphabet_two)
        card_one[i] = alphabet_one
        card_two[i] = alphabet_two
    i += 1

print(f"{card_one=}")
print(f"{card_two=}")

character = input("\nSpot the same symbol: ")
if character == same_symbol:
    print("Correct")
else:
    print("Wrong")
