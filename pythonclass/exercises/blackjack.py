from pprint import pprint
from random import shuffle


class Card():
    # diamonds, hearts, clubs, spades
    SUITS = ("D", "H", "C", "S")
    FACES = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")
    VALUES = {"T": 10, "J": 11, "Q": 12, "K": 14, "A": 15}

    def __init__(self, face, suit):
        if face not in self.FACES:
            raise ValueError(f"Invalid face value: {face!r}")

        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit value: {suit!r}")

        self.face = face
        self.suit = suit

    def __str__(self):
        return f"{self.face}{self.suit}"

    def __repr__(self):
        return f"Card(face={self.face!r}, suit={self.suit!r})"

    def __eq__(self, other):
        return (self.face, self.suit) == (other.face, other.suit)

    def __lt__(self, other):
        return self.value < other.value

    @property
    def value(self):
        """Return the value of a card"""
        if self.face.isnumeric():
            return int(self.face)
        else:
            return self.VALUES[self.face]

class GermanCard(Card):
    # hearts, bells, acorns, leaves
    SUITS = ("H", "B", "A", "L")

class Player(list):
    def __init__(self, name, *cards):
        self.name = name
        for card in cards:
            self.append(card)

    def __str__(self):
        return ", ".join([str(card) for card in self])

    def __repr__(self):
        return f"<Player {self.name} cards={len(self)}>"


class Deck(list):
    SUITS = ("D", "H", "C", "S")
    FACES = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")

    def __init__(self, shuffle=True):
        self.discards = []

        for suit in self.SUITS:
            for face in self.FACES:
                self.append(Card(face, suit))

        self.shuffle()

    def __repr__(self):
        total = len(self) + len(self.discards)
        return f"<Deck cards={len(self)} dicarded={len(self.discards)} total={total}>"

    def shuffle(self):
        shuffle(self)

    def top(self, discard=False):
        if discard:
            return self.discards[-1]
        else:
            return self[0]


class Game():
    def __init__(self, players, cards=3):
        self.deck = Deck()
        self.deal(players, cards)

    def __repr__(self):
        return f"<Game players={len(self.players)}>"

    def deal(self, players, size):
        self.players = {}
        for i in range(1, players+1):
            self.players[i] = Player(i)
            self.draw(self.players[i], size)

    def draw(self, hand, count=1):
        """Remove a number of cards from the deck and add them to a hand."""
        if not isinstance(hand, Player):
            hand = self.player(hand)

        for _ in range(count):
            hand.append(self.deck.pop(0))

    def discard(self, hand, *cards):
        """Remove a card from a hand and add it to the discard pile."""
        if not isinstance(hand, Player):
            hand = self.player(hand)

        for card in cards:
            if isinstance(card, int):
                card = hand[card]
            elif isinstance(card, str):
                card = Card(*card)

            self.deck.discards.append(card)
            hand.remove(card)

    def player(self, name):
        return self.players[name]

def main():
    game = Game(2)

    print(game)
    print(repr(game.players[1]))
    print(game.players[1])
    print(game.deck)

    game.draw(1, 3)
    print(game.players[1])

    game.discard(1, 0)
    print(game.players[1])

    game.player(1).sort()
    print(game.player(1))

    print(game.deck)



if __name__ == "__main__":
    main()


