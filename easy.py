# https://www.hackerrank.com/challenges/py-hello-world/problem

print("Hello, World!")

# https://www.hackerrank.com/challenges/py-if-else/problem#

number = int(input())
weird = "Weird"
n_weird = "Not Weird"


def isEven(number):
    return number % 2 == 0


def inRange(number, start, end):
    return number >= start and number <= end


if not isEven(number):
    print(weird)
elif isEven(number) and inRange(number, 2, 5):
    print(n_weird)
elif isEven(number) and inRange(number, 6, 20):
    print(weird)
elif isEven(number) and number > 20:
    print(n_weird)

# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem

a = int(input())
b = int(input())

add = a + b
subtract = a - b
multiply = a * b

print(add, subtract, multiply, sep="\n")

# https://www.hackerrank.com/challenges/python-division/problem

a = int(input())
b = int(input())

integer_division = a // b
decimal_division = a / b

print(integer_division, decimal_division, sep="\n")

# https://www.hackerrank.com/challenges/python-loops/problem

end = int(input())

for index in range(0, end):
    print(index**2)

# https://www.hackerrank.com/challenges/python-print/problem

size = int(input())

for index in range(1, size + 1):
    print(index, end="")

# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

size = int(input())
numbers = list(map(int, input().split(" ")))

maximum = max(numbers)
second_maximum = -1000

for number in numbers:
    if number > second_maximum and number < maximum:
        second_maximum = number

print(second_maximum)

# https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(a**b + c**d)

# https://www.hackerrank.com/challenges/list-comprehensions/problem

x = int(input())
y = int(input())
z = int(input())
n = int(input())

possibilities = [[a, b, c] for a in range(
    0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != n]

print(possibilities)
