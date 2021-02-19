from pythonclass.lessons.greeting import greeting

def test_greeting_fail():
    assert greeting("buffy") == "", \
        'demo of a test failure'

def test_greeting_lower():
    assert greeting("buffy") == "Welcome Buffy.", \
        'should return "Welcome Buffy." with the lowercase name capitalized.'


def test_greeting_upper_to_title():
    assert greeting("XANDER") == "Welcome Xander.", \
        'should return "Welcome Xander." with all caps name capitalized.'


def test_greeting_multi_word():
    assert greeting("SpongeBob SquarePants") == "Welcome Spongebob Squarepants.", \
        'should return "Welcome Spongebob Squarepants." with all words capitalized.'


def test_greeting_empty_string():
    assert greeting("") == "Welcome.", \
        'should return "Welcome." if name is empty.'


def test_greeting_blank():
    assert greeting("  ") == "Welcome.", \
        'should return "Welcome." if name just whitespace.'


def test_greeting_number():
    assert greeting("42") == "Welcome 42.", \
        'should return "Welcome 42." no special handling for numbers.'
