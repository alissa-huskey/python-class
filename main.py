from datetime import datetime

# this is a comment
"""
this is also a comment
but it can span multiple lines, surrounded by three double-quotes
"""


# variables are assigned with
# <variable-name> = <value>
# the variable name has no quotes
# a variable must start with letters or _ and
# can include letters, numbers, _
example_variable = "value"
_variable = "abc"

# strings are defined with either ' or ""
something = "nothing"
something = 'nothing'

# boolean values are defined as True or False
# they are not surrounded by quotes, and must be capatilized
isFun = True
isFun = False

"""
function calls are done like <functionName>(<arguments>)
Some functions don't take any arguments, like this:
  doThing()
Some take multiple arguments seperated by commas like this:
  setBirthdate(1988, 7, 12)
Here the function name is print
  the argument is "Welcome to PyPet"
"""
print("Welcome to PyPet")

"""
this is an if statement
the structure is
  if <condition>:
    <block>
  elif <condition>:
    <block>
  else:
    <block>
A condition is a piece of code that will evaluate to
  either True or False
Some examples are:
    today == person["birthdate"]    # is equal
    name != "Alissa"                # not equal
    age < 21                        # less than
    bac > 0.8                       # greater than
"""
if datetime.now().hour < 12:
    print("Good morning")
elif datetime.now().hour < 16:
    print("Good afternoon")
else:
    print("Good evening")

"""
this is a function definition
the structure is
def <function-name>(<optional-arguments>):
 <block>
the function starts here
"""
def feed(pet):
  # this is an if statement
  if pet["isHungry"] == True:
     # these lines will only run if the above is true
    print("Feeding: " + pet["name"])
    pet["isHungry"] = False
    pet["weight"] = pet["weight"] + 1
  else:
    # otherwise, this line will run
    print(pet["name"] + "is not hungry, thanks anyway.")
"""
the function ends here
a function ends when the indentation is reduced
or when it is followed by a blank line
a section of code like that is called a block
and it works the same for if-statements, for-loops, while-loops and more
"""

def exercise(pet):
  # this shows how to combine multiple strings together
  #   using a + between the strings
  #   this is called string concatenation
  print("Taking " + pet["name"] + " for some exercise")
  pet["weight"] = pet["weight"] - 1
  pet["isHungry"] = True

def punish(pet):
  print("Bad " + pet["name"] + "!")
  pet["happy"] = False

def treat(pet):
  print("Good " + pet["name"] + "!")
  pet["happy"] = True
  pet["weight"] = pet["weight"] + 2

"""
this function returns a value
so that when you call it, you can assign the result to
a variable like this:
<variableName> = menu()
"""
def menu():
  print()
  print("[p]unish")
  print("[t]reat")
  print("[e]xercise")
  print("[f]eed")
  print("[q]uit")
  # the input() function waits for the user to enter text and
  # and returns that text
  # it takes a string as an argument, which will be printed
  # before the users cursor
  response = input("> ")
  # this line is what returns a value
  # the format is return <value>
  return response

"""
this is a dictionary
The structure is
<variableName> = {
  <key>: <value>,
}
It must be surrounded by {},
  have a : between each key and value,
  and each pair is seperated by commas
In this case, the keys are strings,
  so the keys must be quoted.
"""
cat = {
  "name": "Flufosourus",
  "happy": True,
  "age": 5,
  "weight": 7,
  "isHungry": True,
  "pic": "(=^o.o^=)__",
}

fish = {
  "name": "Scaley",
  "age": 1,
  "happy": False,
  "weight": 0.5,
  "isHungry": False,
  "pic": "<`)))><",
}

"""
this is a list
The structure is
  <variableName> = [ <value>, <value> ]
The values in the list are seperated with
  commas like in a dictionary
  except in a list, there are no keys
"""
pets = [ cat, fish ]

"""
this is a for-loop
the structure is
for <list-item> in <list>:
 <block>
Just like in functions and if-statements
  the lines that are run as a part of the loop
  are the ones that are indented
"""
for minion in pets:
  print("Hello from " + minion["name"] + "!" + "  " + minion["pic"])

print()
response = ""

"""
this is a while-loop
the structure is
while <condition>:
 <block>
Like a for-loop, it will keep looping over the same block of code
  But it uses a conditional like in an if-statement to determine
  when to stop looping
In this case, I use it to keep printing the menu, getting input
    from the user, and acting on it
    as long as the response variable is not set to the value "q".
"""
while response != "q":
  response = menu()
  for minion in pets:
    if response == "p":
      punish(minion)
    elif response == "t":
      treat(minion)
    elif response == "e":
      exercise(minion)
    elif response == "f":
      feed(minion)
    elif response == "q":
      break
    else:
        print("Sorry, I don't know what you mean.")
    print(minion)

""" this is also a commment
that ends here
"""

# everything below this will never run
# because if False will never be true
if False:
  print("pet info:")
  print(cat)
  print()
  feed(cat)
  print("after feeding:")
  print(cat)
  print()
  exercise(cat)
  print("after exercise:")
  print(cat)
  print()
