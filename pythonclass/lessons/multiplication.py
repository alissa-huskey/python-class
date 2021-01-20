"""Print a 9x9 multiplaction table

An exercise from the loops lesson:
https://alissa-huskey.github.io/python-class/lessons/loops.html

"""

SIZE = 9

def main():
    print()

    x = 1
    while x <= SIZE:
        print("  ", end="")
        y = 1
        while y <= SIZE:
            val = x * y
            print(str(val).rjust(4), end="  ")
            y += 1
        x+=1
        print("\n")

main()
