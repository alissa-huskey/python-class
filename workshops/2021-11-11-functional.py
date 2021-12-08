"""2021-11-11 Functional Programming
https://alissa-huskey.github.io/python-class/lessons/data/functional-programming.html

Data & In-Depth
---------------
-Brian

"""

# Functional programming intro

months = ["january", "february", "march"]

## proceedural

revised = []

for month in months:
    revised.append(f"{month[:3].title()}")

print(revised)

## functional

def shorten(month):
    return f"{month[:3].title()}"

revised = map(shorten, months)

revised = map(lambda month: month[:3] , months)
revised = map(lambda month: f"{month.title()}" , revised)

print(list(revised))

## filter

days = ["mon", "tue", "wed", "thurs", "fri", "sat", "sun"]

weekend = filter(lambda day: day.startswith("s"), days)

print(list(weekend))


# reduce

total = 0
for i in range(1, 10):
    total += i

print(total)
    
from functools import reduce

def add(result, current):
    return result + current

from operator import add

total = reduce(add, range(1, 10))
total = reduce(lambda res, cur: res + cur, range(1, 10))

# default initial value
# result of called type of first item in iterable
#
# first item: 1
# type:       int
# called:     int()
#             0

print(total)

#
total = reduce(lambda res, cur: res + str(cur), range(1, 10), "")

print(total)

from collections import defaultdict

things = (5, 5, 16, 7, 7, 8, 9, 9, 10)

def count(res, cur):
    print("cur is:", cur)
    print("res is:", res)
    res[cur] = things.count(cur)
    return res

groups = reduce(count, things, {})

print(groups)





