import math

def amount_of_combinations():
    cards = 52
    hand = 5

    result = math.factorial(cards) / (math.factorial(hand) * math.factorial(cards - hand))
    print(result)

amount_of_combinations()