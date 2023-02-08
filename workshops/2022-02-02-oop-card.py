"""
2022-02-02 In-Depth -- Card class OOP

Attendees
---------
- Brian

Agenda
------
* review & warmup
    - basic OOP with a Card class
    - dunder methods (__repr__, __str__, __eq__)
    - pytest tests
    - behavior driven development

    [ ] make a Card class that takes a face and suit in its constructor
    [ ] suits are: D, H, C and S
    [ ] faces are: 2-9 and T, J, K, A
    [ ] when converted to a string using str(), it should print the two characters
        representing its face and suit. ie: "TS"
    [ ] when converted to a string using repr(), it should show the code to make
        that object, ie: Card("T", "S")
    [ ] define a __eq__ method that will determine if two cards are equal. In
        addition to self, it should take one argument, other, which represents the
        other card object.
    [ ] write pytest tests to ensure that things work as expected
    
* properties
    - the builtin @property decorator

    [ ] add a value property that returns the an integer value for the face
    [ ] define a __lt__ method that determins if other_card is less than self
        depending on the value


"""
