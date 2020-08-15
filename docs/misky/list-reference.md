Lists
=====


    day_names = [
        "sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"
    ]
Creating Lists
--------------

mylist = list()                           # create an empty list
mylist = []                               # create an empty list
mylist = [ 1, 2, 3 ]                      # create a list with elements 1, 2 and 3


List Index Addresses
--------------------

mylist[0]                                 # first element
mylist[1]                                 # second element
mylist[-1]                                # last element


List Slices
-----------


mylist[<start-index>:<stop-index>]
mylist[1:3]                               # section of the list, starting at
mylist[1:]                                # the list except for the first element
mylist[:-1]                               # the list except for the last element


Accessing List Elements
-----------------------

mylist[0]                                 # return the value at index
mylist.index("bacon")                     # get the index number of value "bacon"


Changing List Elements
----------------------

mylist[0] = "eggs"                        # update value by index
del mylist[2]                             # remove an element by index
mylist.insert(0, "pancakes")
mylist.append("tacos")                    # add an element to the end of the list
mylist.remove("bacon")                    # remove element by element
mylist.pop()                              # remove and return the last element



Iterating through List Contents
-------------------------------

for elm in mylist:
  print(elm)

for i, elm in enumerate(mylist):
  print(i, elm)


List Information
----------------

len(mylist)
max(mylist)
min(mylist)
min(mylist)
sum(mylist)
mylist.count("purple")


Checking List Membership
------------------------

elm in mylist


Modifying Lists
---------------

list.sort()
list.reverse()


Converting To/From Lists
-------------------

list("string")
"\n".join(mylist)



Exercises
---------

* Make a list of 3-5 lunch specials items, then print the list with the a number one special per line.
* Make a list of month names. Ask the user for their birthday then print the formatted month name and day.
* You started with \$210. You spent \$32.83 on gas, \$15.27 on lunch, and
  \$123.52 on groceries, and were paid back a loan of \$25. Use a list to
  calculate your balance.
* Start with an empty list. Add the following one at a time using the index to
  put them in the correct order. Add your birthday, Christmas, and the
  anniversary of your last move in the correct order.
