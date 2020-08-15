#!/usr/bin/env python3

"""
Between 1 and 1000, there is only 1 number that meets the following criteria:

- The number has two or more digits.
- The number is prime.
- The number does NOT contain a 1 or 7 in it.
- The sum of all of the digits is less than or equal to 10.
- The first two digits add up to be odd.
- The second to last digit is even and greater than 1.
- The last digit is equal to how many digits are in the number.

https://github.com/jorgegonzalez/beginner-projects#change-calculator

"""

for num in range(10, 1000):
    digits = [int(n) for n in list(str(num))]

    # does NOT contain a 1 or 7 in it.
    if 7 in digits or 1 in digits:
        continue

    # The sum of all of the digits is less than or equal to 10.
    if sum(digits) > 10:
        continue

    # The first two digits add up to be odd.
    if sum(digits[:2]) % 2 == 0:
        continue

    # The second to last digit is even and greater than 1.
    if digits[-2] % 2 == 1 or digits[-2] <= 1:
        continue

    # The last digit is equal to how many digits are in the number.
    if digits[-1] != len(digits):
        continue

    # is not a prime number
    if any(num % i == 0 for i in range(2, num)):
        continue

    # the number
    print(f"The number is: {num}")
