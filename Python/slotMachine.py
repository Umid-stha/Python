import random
from curses.ascii import isdigit
MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbolCount={
    "A": 2,
    "B": 4,
    "C": 5,
    "D": 6
}

symbolValue={
    "A": 5,
    "B": 2.5,
    "C": 2,
    "D": 1.5
}

#Slot machine mechanisims

def checkWinnings(columns, lines, bet, value):
    Winnings = 0
    winningLines = []
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbolToCheck=column[line]
            if symbol != symbolToCheck:
                break
        else:
            Winnings += value[symbol] * bet
            winningLines.append(line+1)
    return Winnings, winningLines

def getSlotMachineSpin(rows, cols, symbols):
    allSymbols = []
    for symbol, symbolCount in symbols.items():
        for i in range(symbolCount):
            allSymbols.append(symbol)
    columns= []
    for col in range(cols):
        column=[]
        currentSymbol=allSymbols[:]
        for row in range(rows):
            value = random.choice(currentSymbol)
            currentSymbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def printSlotMacine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row], "|", end=" ")
            else :
                print(column[row])
        
#User inputs

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

#main game

def game(balance):
    lines=getNumOfLines()
    while True:
        bet=getBet()
        totalBet=lines*bet
        if totalBet>balance:
            print(f"You dont have enough balance to bet. your current balance is {balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines, Your total bet is ${totalBet}")
    print("here is the slot machine: ")
    slots=getSlotMachineSpin(ROWS, COLS, symbolCount)
    printSlotMacine(slots)
    winning, winningLines=checkWinnings(slots, lines, bet, symbolValue)
    print(f"you have won ${winning} from this roll")
    print(f"you won on lines: ", *winningLines)
    return winning-totalBet

def main():
    balance=deposit()
    while True:
        print(f"Your current balance is {balance}")
        spin=input("Press Enter to play(q to quit)")
        if spin=="q":
            break
        else:
            balance += game(balance)
    print("Your current balance is ${balance}")
main()