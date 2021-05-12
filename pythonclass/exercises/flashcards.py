"""Flashcards exercise"""

from pathlib import Path

def run_flashcard():
    ...

def create_card():
    dirpath = Path(__file__).parent.parent / "data" / "cards"
    dirpath.mkdir(exist_ok=True)
    question = input("Question: ")
    answer = input("Answer: ")

    print(f"Question: {question}")
    print(f"Answer: {answer}")

    ok = input("Is this correct? [y/N] ")
    if not ok:
        return

    card_num = len(list(dirpath.iterdir())) + 1
    card_path = dirpath / f"card_{card_num}.txt"
    with open(card_path, "w") as fp:
        fp.write(f"{question}\n")
        fp.write(f"{answer}\n")

    print(f"Created card #{card_num}")

def main():
    menu = [
        "create card",
        "run flashcards",
    ]

    options = { x[0]: x for x in menu }

    while True:
        for option in menu:
            print(f"[{option[0]}]{option[1:]}")

        reply = input("> ")
        choice = reply.lower()

        if choice not in menu:
            choice = options.get(choice, None)

        if not choice:
            print(f"Invalid option: {reply}")
            continue
        fn = globals()[choice.replace(" ", "_")]
        fn()

main()
