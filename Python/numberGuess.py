import random

numberToGuess=random.randint(1,100)

print("Welcome to number guess game. You get 10 tries to guess the number between 1-100")
count=0

while count<=10:
    guess=int(input("guess any number from 1-100"))
    count +=1
    if guess==numberToGuess:
        print(f"you have guess the correct number in {count} attempts")
        break
    elif guess>numberToGuess:
        print("your guess is higher than number to guess")
    elif guess<numberToGuess:
        print("your guess is lower than number to guess")
    elif count>=10:
        print("you are out of retries")
        break