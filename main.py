import random

players, dealers = [], []


def dealcard():
    """This function is to pick a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    card = random.choice(cards)
    return card


def scoring(hand):
    """This is to check whether a ace is in the player or dealers deck.
    if their is the card will be manipulated"""
    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)


def validator():
    """This is the outcome of the player and dealers deck"""
    if sum(players) > 21:
        print("You Lose")
    elif sum(dealers) > 21:
        print("You Win")
    elif sum(players) == sum(dealers):
        print("Tie")
    elif sum(players) < sum(dealers):
        print("You Lose")
    else:
        print("You Win")


def current():
    """Displays the player and dealer current deck of cards"""
    print("Current hands!")
    print(f"Dealers {dealers}")
    print(f"Players {players}")


def intialize():
    """This draw the first two cards for the player and dealer"""
    for i in range(2):
        players.append(dealcard())
        dealers.append(dealcard())
    scoring(players)
    scoring(dealers)
    current()


def playerDraw():
    """Allows the player to draw cards """
    print("Would you like more cards added type y or n:")
    x = input()
    while x == "y" and sum(players) < 21:
        players.append(dealcard())

        scoring(players)
        current()
        if sum(players) < 21:
            x = input("Would you like more cards added? Type y or n: ")


def dealersDraw():
    """Allows the dealer two draw cards """
    while sum(players) <= 21 and sum(dealers) < 17:
        dealers.append(dealcard())
        scoring(dealers)


def main():
    intialize()
    playerDraw()
    dealersDraw()
    current()
    validator()

main()
