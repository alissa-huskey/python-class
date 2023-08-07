"""Dictionary lesson lecture"""

numbers = {
    'I' : 1,
    'II': 2,
}

numbers['III'] = 3

print("numbers:", numbers)
print("numbers['II']:", numbers["II"])


print("getting 'I'", numbers.get("I", 0))
print("getting 'V'", numbers.get("V", 0))

numbers['II'] = 200

print("numbers:", numbers)

del numbers['II']

print("(after del) numbers:", numbers)

num = numbers.pop("I", "unknown")

print("num:", num)
print("(after .pop()) numbers:", numbers)

print(numbers.keys())
print(numbers.values())

# key in dict.keys()

if "II" in numbers.keys():
    print("We have a II!")
elif "I" not in numbers.keys():
    print("We're missing a I!")

"III" not in numbers.keys()

numbers = {
    'I' : 1,
    'II': 2,
    'III': 3,
    'IV': 4,
    'V': 5,
}

for element in numbers:
    value = numbers[element]
    print(f"key: {element}, value: {value}")

for roman, numeric in numbers.items():
    print(f"the roman numeral {roman} has the value: {numeric}")
