"""A hangman game

An exercise from the loops lesson:
https://alissa-huskey.github.io/python-class/lessons/loops.html
"""

import random

WORDS = [ "hello", "goodbye", "secret", "satisfy", "apple", "bear" ]

def info(turn, chances, guess):
    """print the used vs unused chances and guessed vs unguessed letters
       example:
           chances: xx____ 7 letters: _e_____
    """
    print(" "*40, "chances:", ("x"*turn)+("_"*(chances-turn)), len(guess), "letters:", guess)

def main():
    """."""
    turn, chances, word = 1, 6, random.choice(WORDS)
    guess = "_" * len(word)

    info(0, chances, guess)

    while guess != word and turn <= chances:
        char = input("Guess a letter: ").lower()
        if not char:
            continue
        elif len(char) > 1:
            print(" Just one letter!")
            continue
        if char in word:
            letters = list(guess)
            for i,c in enumerate(word):
                if c == char:
                    letters[i] = c
            guess = "".join(letters)
        print(" "*40, "chances:", ("x"*turn)+("_"*(chances-turn)), len(word), "letters:", guess)
        turn += 1
    if guess == word:
        print("You win!!")
    else:
        print("Too bad. The word was:", word)

main()
