#!/usr/bin/env python3

"""
Script to demonstrate list basics
See also: https://www.tutorialspoint.com/python/python_lists.htm
"""

def header(msg):
    print("\n", msg)
    print("-"*50)

# creating lists ------------------------------------------------------

mylist = list()
mylist = []
mylist = ['a', 'b', 'c', 'd', 'e']

# list index addresses ------------------------------------------------

mylist[0]             # first list item
mylist[1]             # second list item
mylist[-1]            # last list item

# example: list index addresses ---------------------------------------

from datetime import datetime
days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

header("example: list index addresses")
today = datetime.now().weekday()

print("the third day of the week is:", days[2])
print("today is:", days[today])

# list iteration ------------------------------------------------------

header("for <elm> in <list>")
for elm in mylist:
    print(elm)


header("for <i>, <elm> in enumerate(<list>)")
for i, elm in enumerate(mylist):
    print(f"{i}:", elm)

# example: list iteration ---------------------------------------------

colors = ["red", "green", "blue"]

header("colors")
for color in colors:
    print(color)

# exercise: list iteration --------------------------------------------

"""
* Make a list of 3-5 colors, cities or lunch specials then print one per line
"""

# sean
# ----

header("sean's lunch specials")
lunch_specials = [
    "ham-dogs",
    "hot burgers",
    "Donut Bucket",
    "chicky tendies",
    "Unfortunate tuna"
]

for lunch_special in lunch_specials:
    print(lunch_special)

# jayson
# ------

header("jayson's cities")
# cities_that_are_special = ("Oceanside", "Oakland", "Denver")
# cities_that_are_special[3] = "Denver"
cities_that_are_special = ["Oceanside", "Oakland", "Denver"]
cities_that_are_special.append("Escondido")
for city in cities_that_are_special :
    print(city)

# exercise: list iteration with enumerate() ---------------------------

"""
* Make a list of 3-5 ranked favorite movies, books, songs, or something. Print
* each one on a line with the number next to it.

"""

header("ranked favorite movies")

fav_movies = ["the prestige", "fight club", "the prophecy"]

for num, movie in enumerate(fav_movies):
    print(f"#{num+1}:", movie)

# sean
# ----

header("sean's ranked favorite movies")
fav_movies = ["almost famous", "apocalypse now", "persepolis", "infinity war"]
for num, movie in enumerate(fav_movies):
    print(f"#{num+1}:", movie)


# jayson
# ------

header("jayson's ranked favorite movies")
fav_seanisms = ["I'd do things that make god and robots cry", "goodbye forever", "See you in hell", "too late now asshole"]
for rank, seanism in enumerate(fav_seanisms):
    print(f"#{rank+1}:", seanism)
#period combination of functions and variables? """Carry on my wayward son"""

# converting strings <--> lists ---------------------------------------

# convert a string into a list of characters
chars = list("abc")                            # ['a', 'b', 'c']

# split a string on whitespace
words = "red green blue".split()               # ['red', 'green', 'blue']

# split a string on another delim
url = "github.com/alissa-huskey/python-class"
url_parts = url.split("/")                     # ['github.com', 'alissa-huskey', 'python-class']

# list to string
chars = ['H', 'e', 'l', 'l', 'o']
word = "".join(chars)                          # "Hello"

# list to string with delim between elements
fileparts = ['~', 'python-class', 'README.md']
path = "/".join(chars)                         # ~/python-class/README.md

# example: converting strings <--> lists ------------------------------

header("strings to lists: list(<string>)")

"""strings to lists: convert strings to list of characters"""
name_str = "alissa"
name_list = list(name_str)
name_list[0] = name_list[0].upper()
name = "".join(name_list)
print(f"{name_str} -> {name}")

"""
strings to lists: split a string into a list of words (split by whitespace)
ie: Make Sean Shakespearian
"""

header("strings to lists: <string>.split([<delim>])")
menu_items = "open print quit".split()
print(menu_items)

header('strings <--> lists: <string>.split([<delim>]) ; "<delim>".join(<list>)')
sentence = "I'd do things that make god and robots cry"
words = sentence.split(" ")
words.sort(reverse=True)
new_order = " ".join(words)
print(new_order)

# exercise: strings <--> lists ----------------------------------------

"""
1. Start with a string, print it
2. Convert it to a list, print it
3. Change the list somehow, print it
4. Turn it back into a string, print it
"""

header("sean's string->list->string")
varname = list("my body left for the summer")
varname.sort()
print(varname)

mystr = "werds are for nerds"
nerdy = mystr.split()
nerdy.sort()
print(nerdy)

sentence = "+".join(nerdy)
print(sentence)

header("jayson's string->list->string")
myswellvar = "golly gee wilikers Mr. Peabody!"
myswellvar = myswellvar.split()
myswellvar.sort()
print(myswellvar)
childabuse = " ".join(myswellvar)
print(childabuse)

print()

# rabbit trail: method chaining ---------------------------------------

header("rabbit trail: method chaining")

# val = input("tell me! ").lower()
# val = input("tell me! ").lower().strip().sub('.txt', '').center("100")
# print(val)

# rabbit trail: list.sort() -------------------------------------------

# this will NOT work because sort() returns None
wrong_letters = list("abcde").sort()

# this will work
letters = list("abcde")
letters.sort()             # returns None, changes the order of letters
print(letters)
