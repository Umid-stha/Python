from curses.ascii import isdigit
import random

MAX_BET=100
MIN_BET=1

cardSuits = ["Diamond", "Spade", "Club", "Heart"]
Values=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

cardValues={
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': [1, 11]
}

def createDeck(suits,values):
    deck=[]
    for suit in suits:
        for value in values:
            deck.append({"value":value, "suit":suit})
    return deck

def shuffleDeck(deck):
    random.shuffle(deck)
    return deck

'''def deposit():
    while True:
        amount=input("Enter the amount you want to deposit: $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("please enter amount greater than 0")
        else:
            print("Please enter a number")
    return amount'''

'''def getBet():
    while True:
        bet=input("How much money do you want to bet: $")
        if bet.isdigit():
            bet=int(bet)
            if MIN_BET <= bet <=MAX_BET:
                break
            else:
                print(f"Please enter a valid bet from {MIN_BET} to {MAX_BET}")
        else:
            print("Please enter a number")
    return bet'''

def main():
    '''balance=deposit()
    bet=getBet()'''
    deck=createDeck(cardSuits, Values)
    shuffledDeck=shuffleDeck(deck)
    #print(deck)
    print(shuffledDeck)
main()