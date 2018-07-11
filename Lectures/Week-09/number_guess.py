import numpy as np

print('Try to guess my number between 1 and 10')

number = np.random.randint(1, 11)
guess = None

while guess != number:
    guess = int(input('Guess: '))

    if guess > number:
        print('Your guess was too high.')

    elif guess < number:
        print('Your guess was too low.')

    elif guess == number:
        print('You did it! My number was ', number)
