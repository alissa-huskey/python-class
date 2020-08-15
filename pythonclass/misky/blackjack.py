#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Blackjack Game
https://bicyclecards.com/how-to-play/blackjack/

- Objective:
    Each participant attempts to beat the dealer by getting a count as close to
    21 as possible, without going over 21.

- Card Values:
    - Ace is worth 1 or 11
    - Face cards are 10
    - Any other card is its pip value.

  Hole = the dealer’s card that is face down

- Setup:
    - A standard 52-card pack is used for the desk or optionally six decks.
    - Each player places a bet within within designated limits, (ex $2 min,
      $500 max.)
    - The dealer deals two cards face up to each player. The dealer receives
      one card face up and one face down.

- The Play:
    - Each player chooses repeeatedly to:
        - hit: get dealt another card
        - stand: not ask for another card
        after your first two cards:
            - double down: double your bet, then receive only one more card
        if your first two cards have the same value:
            - split: seperate your cards and a card to make both a complete
              hand and bet an equal amount on the second hand. Each hand is then
              played seperately.
    - Turn ends when:
        - player chooses "stand"
        - or they go "bust": the total is over 21

- The Dealer's Play:
    - The dealer's face-down card is turned face-up
    - The dealer will repeatedly:
        - stand if the total is 17 or more
        - hit if the total is 16 or less

- Settling:
    - win:            dealer bust or player higher than dealer  pays  1:1
    - blackjack win:                                            pays  3:2
    - lose:           player bust or lower than dealer          chips lost
    - push:           player and dealer blackjack               no chips lost or paid
"""

# ### Imports ################################################################


# ## Global Variables ########################################################



# ## Functions ###############################################################

def mkdeck():
    """Return a deck of 52 cards"""


def deal(deck, is_dealer=False):
    """Deal a blackjack hand"""


# ## Runner ##################################################################

def main():
    """Blackjack"""
    print("Well, hello.")
    deck = mkdeck()

    dealer_hand = deal(deck, is_dealer=True)
    player_hand = deal(deck)

    player_play(player_hand)

    if player_hand['status'] != "bust":
        dealer_play()





if __name__ == "__main__":
    main()
