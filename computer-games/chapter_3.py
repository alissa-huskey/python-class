#!/usr/bin/env python3
"""
This is a Guess the Number game
Inspired by:  http://inventwithpython.com/invent4thed/chapter3.html
"""

import random

number = random.randint(1, 20)
max_guesses = 6

player = input("Hello! What is your name? ")
print("Hello " + player + ".")
print("I am thinking of a number between 1 and 20.")
print()

for guess_count in range(1, max_guesses):
    print("Guess ", guess_count, "of", max_guesses)
    guess = input("Your guess: ")
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')

    elif guess > number:
        print('Your guess is too high.')

    else:
        break

    print()

if guess == number:
    guess_count = str(guess_count)
    print('Good job, ' + player + '! You guessed my number in ' + guess_count + ' guesses!')

else:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
