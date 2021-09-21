from random import randint

def rand_nums(amount=10, ceil=500):
    """Return a list of random positive and negative ints and floats"""
    numbers = []
    for _ in range(amount):
        # get a random float
        num = randint(-ceil, ceil) + (1 / randint(1, 99))

        # randomly make it an int
        if randint(0, 1):
            num = int(num)

        numbers.append(num)

    return numbers
