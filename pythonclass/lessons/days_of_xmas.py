"""Print the 12 Days of Christmas Song

An exercise from the loops lesson:
https://alissa-huskey.github.io/python-class/lessons/loops.html
"""

import time

DAYS = [
    ['first', "a partridge in a pear tree"],
    ['second', "turtle doves"],
    ['third', "french hens"],
    ['forth', "calling birds"],
    ['fifth', "golden rings"],
    ['sixth', "geese a laying"],
    ['seventh', "swans a swimming"],
    ['eighth', "maids a milking"],
    ['ninth', "ladies dancing"],
    ['tenth', "lords a leaping"],
    ['eleventh', "pipers piping"],
    ['twelfth', "drummers drumming"],
]

i = 0

while i < len(DAYS):
    day, gift = DAYS[i]
    print("On the", day, "day of Christmas my true love gave to me")

    x = i
    while x >= 0:
        gift = DAYS[x][1]
        time.sleep(0.5)

        # indent the line
        line = "  "

        # add the "and" in "and a partridge in a pear tree"
        if i and x == 0:
            line += "and "

        # add the number of gifts
        if x:
            line += str(x+1) + " "

        # add the gift given
        line += gift

        # add the "," or "."
        if x:
            line += ","
        else:
            line += "."

        # print the line
        print(line)

        x -= 1

    i += 1

    print()
