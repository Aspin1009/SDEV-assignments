from random import randint

def setTarget():

    target = randint(1,100)

    return target

def guess_number():

    target = setTarget()

    print('Im thinking of a number between 1 and 100.')

    while True:
        try:

            guess = int(input('Enter your guess: '))

            if guess < target:
                print('Your guess is too low. Try again.')
            elif guess > target:
                print('Your guess is too high. Try again.')
            else:
                print(f'You got it right! The correct number was {target}!')
                break
        except ValueError:
                print('Invalid answer. Please try again.')
            
guess_number()              
