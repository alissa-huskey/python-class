"""
2021-12-08 Data & In-Depth -- Aggregate exercises

Attendees
---------
- Fiona
- Brian
"""


def min_letter(text):
    """Return the "lowest" letter in a string"""
    return min(text)

def maxlen(strings):
    """return the max length of a list of strings"""
    sizes = []
    for x in strings:
        sizes.append(len(x))
    return max(sizes)

def all_even(numbers):
    """Return True if all numbers are even"""
    bools = []
    for x in numbers:
        bools.append(x % 2 == 0)
    return all(bools)

def all_even(numbers):
    """Return True if all numbers are even"""
    return all([x % 2 == 0 for x in numbers])

def valid_row(line):
    fields = line.split(",")
    if all(fields):
        print("Valid")
        return True
    else:
        print("All fields must be filled out.")
        return False



def get_guesses():
    guesses = []

    for i in range(1, 5):
        guess = input(f"{i}. Pick a number 1-10: ").strip()
        guesses.append(guess)

    if not all(guesses):
        print("You seem to have missed some!")
    else:
        print("OK!")

    print(guesses)



def main():
    #  print()
    #  print(min_letter("goodbye"))
    #  print(maxlen(["title", "author", "year"]))
    #  get_guesses()
    valid_csv_row("1,2,3")
    valid_csv_row("1,,3")

if __name__ == "__main__":
    main()
