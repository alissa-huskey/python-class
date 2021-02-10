def greeting(name):
    """Return a welcome message string, including formatted name unless it's blank."""
    name = name.strip().title()
    if not name:
        return "Welcome."
    else:
        return f"Welcome {name}."

def test_greeting():
    assert greeting("buffy") == "", \
        'demo of a test failure'

    assert greeting("buffy") == "Welcome Buffy.", \
     'should return "Welcome Buffy." with the lowercae name capitalized.'

    assert greeting("XANDER") == "Welcome Xander.", \
        'should return "Welcome Xander." with all caps name capitalized.'

    assert greeting("SpongeBob SquarePants") == "Welcome Spongebob Squarepants.", \
        'should return "Welcome Spongebob Squarepants." with all words capitalized.'

    assert greeting("") == "Welcome.", \
        'should return "Welcome." if name is blank.'

    assert greeting("  ") == "Welcome.", \
        'should return "Welcome." if name just whitespace.'

    assert greeting("42") == "Welcome 42.", \
        'should return "Welcome 42." no special handling for numbers.'

def main():
    """ask the user their name, then greet them."""
    name = input("What's your name? ")
    print(greeting(name))

if __name__ == "__main__":
    # test_greeting()
    main()
