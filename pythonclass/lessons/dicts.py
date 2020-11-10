#!/usr/bin/env python3

"""
Script to demonstrate dictionary basics
See also: https://www.tutorialspoint.com/python/python_dictionary.htm
"""

def header(msg):
    print("\n", msg)
    print("-"*50)

# creating dictionaries -----------------------------------------------

header("creating dictionaries")

mydict = {}
mydict = dict()
emojis = {'skull': "💀", 'imp': "👿", 'scream': "😱"}
emojis = dict(skull="💀", imp="👿", scream="😱")

print(emojis)

# exercise: creating dicts --------------------------------------------

"""
* Make a book dict with keys 'title', 'author', and 'genre' for a book of your
   choice. Print the dict
"""

# jayson
# ----

# sean
# ----


# accessing dictionary elements ---------------------------------------

header("accessing dictionary elements")

mydict['key']
mydict.get('key', "default")

print(":skull:", mydict['skull'])
print(":smile:", mydict.get('smile', 'no such emoji!')

# exercise: accessing dict elements -----------------------------------

"""
For each of the following, dicts use the `get()` function to print the 'desc'
    value.  If it does not exist print "(blank)".

    * char = {'name': "imp", 'code': "U+1F47F", 'desc': "angry face with horns"}
    * char = {'name': "skull", 'code': "U+1F480"}
"""

# jayson
# ----

# sean
# ----



# changing dictionary elements ----------------------------------------

mydict['key'] = "new value"
mydict.update({'key1': "val1", 'another_key': "another val"})


# removing dictionary elements ----------------------------------------

del mydict['key']
mydict.pop('key', "default if missing")


# changing dictionary elements ----------------------------------------

'somekey' in mydict
'somekey' in mydict.keys()
'someval' in mydict.values()


# iterating over dictionary elements ----------------------------------

for k in mydict:
      pass

for k, v in mydict.items():
      pass
