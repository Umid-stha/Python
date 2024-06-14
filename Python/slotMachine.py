
from curses.ascii import isdigit
MAX_LINES=3
MAX_BET=100
MIN_BET=1


def deposit():
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
    return amount

def getNumOfLines():
    while True:
        lines=input("Enter the lines you want to bet on from 1-"+str(MAX_LINES)+": ")
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <=MAX_LINES:
                break
            else:
                print("please enter a valid number")
        else:
            print("Please enter a number")
    return lines

def getBet():
    while True:
        bet=input("How much money do you want to bet on each Line: $")
        if bet.isdigit():
            bet=int(bet)
            if MIN_BET <= bet <=MAX_BET:
                break
            else:
                print(f"Please enter a valid bet from {MIN_BET} to {MAX_BET}")
        else:
            print("Please enter a number")
    return bet

def main():
    balance=deposit()
    lines=getNumOfLines()
    while True:
        bet=getBet()
        totalBet=lines*bet
        if totalBet>balance:
            print(f"You dont have enough balance to bet. your current balance is {balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines, Your total bet is ${totalBet}")

main()