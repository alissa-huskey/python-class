Loops
=====


% while loop intro
% else
% i=0; i<x; i++
% break
% continue
% pass
% infinte loops
% draw a line

% manual for loops
% the stack?

% countdown
```python
count = 10
while count:
    print(f"{count}...")
    time.sleep(1)
    count -= 1
```

% print a grid of numbers
```python
rows = 4; cols = 4; rnum = 1 ; num = 1
while rnum <= rows:
    cnum = 1
    while cnum <= cols:
        print(str(num).rjust(3), end=" ")
        cnum += 1
        num += 1
    print()
    rnum += 1
```

% multiplication table
```python
print()
x, size = 1, 9
while x <= size:
  print("  ", end="")
  y = 1
  while y <= size:
    val = x * y
    print(str(val).rjust(4), end="  ")
    y += 1
  x+=1
  print("\n")
```

% hangman
```
words = [ "hello", "goodbye", "secret", "satisfy", "apple", "bear" ]
turn, chances, word = 1, 6, random.choice(words)
guess = "_" * len(word)
while guess != word and turn <= chances:
    char = input("Guess a letter: ").lower()
    if not char:
        continue
    elif len(char) > 1:
        print(" Just one letter!")
        continue
    if char in word:
        letters = list(guess)
        for i,c in enumerate(word):
            if c == char:
                letters[i] = c
        guess = "".join(letters)
    print(" "*40, "chances:", ("x"*turn)+("_"*(chances-turn)), len(word), "letters:", guess)
    turn += 1
if guess == word:
    print("You win!!")
else:
    print("Too bad. The word was:", word)
```

% print the number of characters from input
% Bunco
% https://en.wikipedia.org/wiki/Bunco

