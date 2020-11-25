String Formatting
=================

Reference
---------

* [A Guide to the Newer Python String Format Techniques](https://realpython.com/python-formatted-output/#the-string-format-method-simple-replacement-fields)

Invocation
-------

```python
f"Hello {name}"                                             # f-strings
"Hello %s" % name                                           # interpolation operator: %
"Hello {0}".format(name)                                    # str.format()

format(name, "s")                                           # builtin format()
```

Referencing
-------


```python
"Hello {} {}".format(first_name, last_name)                 # implicit positional
"Hello {0} {1}".format(first_name, last_name)               # explicit positional
"Hello {first} {last}".format(first="John", last="Smith")   # keyword


# dicts by keys
"Hello %(first_name), %(last_name)" % person
"Hello {first_name}, {last_name}".format(**person)
"Hello {first_name}, {last_name}".format_map(person)

# lists by index
"Brought to you by the letter {0}, and by the number {1}.".format(*chars)
```

Type Conversion Codes
---------------------

|   |  d     | *    | int                                      | int
| # |  b     | .f() | binary                                   | int
| # |  f, F  | *    | float (lower, upper)                     | int, float, %:str
| # |  o     | *    | octal                                    | int
| # |  x, X  | *    | hexadecimal (lower, upper)               | int

| # |  e, E  | *    | exponential (lower, upper)               | float, int
| # |  g, G  | *    | float or exponential (lower, upper)      | float, int
| # |  %     | .f() | percentage                               | .f(): float, int


| # |  s     | *    | string                                   | str, %:int, float
|   |  c     | *+   | character                                | int, %:str
| # |  r     | %    | repr                                     | %:all
| # |  a     | %    | ascii                                    | %:all


```python
# numbers
format(255, "d")             # 255
format(.2, ".0%")            # 20%
format(255, "f")             # 255.000000
"%d" % 255.25                # 255
format(float('nan'), "F")    # NAN
format(255, "#.0f")          # 255.
format(255, "b")             # 11111111
format(255, "#b")            # 0b11111111
format(255, "x")             # ff
format(255, "X")             # FF
format(255, "#x")            # 0xff
format(255, "o")             # 377
format(255, "#o")            # 0o377
format(255, "e")             # 2.550000e+02
format(255, "E")             # 2.550000E+02
format(255, ".0e")           # 3e+02
format(255, "#.0e")          # 3.e+02
format(123456, "g")          # 123456
format(1234567890, "g")      # 1.23457e+09
format(1234567890, "G")      # 1.23457E+09
format(1234567890, ".0g")    # 1e+09
format(1234567890, "#.0g")   # 1.e+09

# strings
format("hello", "s")         # hello
format(97, "c")              # a
"%c" % "a"                   # a
"{!r}".format("hello")       # 'hello'
"%r" % "hello"               # 'hello'
"{!a}".format("Pythön")      # Pyth\\xf6n
"%a" % "Pythön"              # Pyth\\xf6n
```



Format Specifier
----------------

```python

f"{myval=}"                    # myval=255
f"{myval = }"                  # myval = 255

# numbers
#  [debug][:[[fill]align][sign][#][0][min-width][group-delim][.prec][d|b|f|F|o|x|X|e|E|g|G|%|s|c]]
#  [ = ][:[[char]<|>|^|=][+|-| ][#][0][number][,_][.number][type]]

# [fill: ][align:>][width:8][type:d]                             # char pad int
"{: >8d}".format(12)                                             # '      12'

# [fill: ][align:>][min-width:4,5][prec:1][type:f]               # char pad floats
format(12.134, "> 6.2f")                                         # ' 12.13'

# [align:>][0][min-width:4,5][prec:1][type:f]                    # zero-pad floats
format(12.134, ">04.1f")                                         # '12.1'
format(12.134, ">05.1f")                                         # '012.1'

# [fill: ][align:=][sign:+,-][width:8][type:d]                    # printing signs
format(12, " =+8d")                                               # '+     12'
format(12, " =-8d")                                               # '      12'
format(-12, " =-8d")                                              # '-     12'

# [group-delim:,]                                                 # thousands seperator
format(1000, ",")                                                 # '1,000'
# [fill: ][group-delim:,][prec:2][type:f]
format(80000, " 6,.2f")                                           # ' 80,000.00'

# [prec:0][type:%]                                                # percentage
format(.2, ".0%")                                                 # '20%'

# [fill: ][align:>][sign:-][group-delim:,][prec:2][type:f]  # curency
"${: >-9,.2f}".format(-202.34)                              # '$  -202.34'
"${: >-9,.2f}".format(1035.87)                              # '$ 1,034.87'
"${: >-9,.2f}".format(25)                                   # '$    25.00'
"${: >-9,.2f}".format(.50)                                  # '$     0.50'






# strings
#  [debug][!conversion][:[[fill]align][min-width][.max-width][type]]
#  [ = ][!s|r|a][:[[char]<|>|^][number][.number][type]]


```


