# Guess the number game
import random
print('Hello!,What is your name?')
name = input()
secretNumber = random.randint(1,10)
print('Well',name,'I am thinking of a number between 1 to 10')

# Asking user to guess the number with 6 max chances to guess

for chancesTaken in range(1,7):
    print('Guess the number quick!!')
    guessedNumber = int(input())
    if guessedNumber > secretNumber :
        print('Your Guess is too high.')
    elif guessedNumber < secretNumber :
        print('Your Guess is too low.')
    else :
        break
print('-------------------------------------------')
if guessedNumber == secretNumber :
    print('Great',name+'!! :). You Guessed it correctly')
else :
    print('Try again',name+'!! :(','\nThe Number I was thinking of was',secretNumber)

print('-------------------------------------------\n')
