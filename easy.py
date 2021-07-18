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

# https://www.hackerrank.com/challenges/nested-list/problem

results = []
grades = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    results.append([name, score])
    grades.append(score)

second_min = sorted(list(set(grades)))[1]
students = []

for result in results:
    if result[1] == second_min:
        students.append(result.pop(0))

for student in sorted(students):
    print(student)

# https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()
grades = student_marks[query_name]
average = sum(grades) / len(grades)
print(f"{average:.2 f}")

# https://www.hackerrank.com/challenges/python-lists/problem

operations = int(input())


def insert(numbers, index, number):
    numbers.insert(index, number)


def print_out(numbers):
    print(numbers)


def remove(numbers, number):
    numbers.remove(number)


def append(numbers, number):
    numbers.append(number)


def sort(numbers):
    numbers.sort()


def pop(numbers):
    numbers.pop()


def reverse(numbers):
    numbers.reverse()


functions = {
    "insert": insert,
    "print": print_out,
    "remove": remove,
    "append": append,
    "sort": sort,
    "pop": pop,
    "reverse": reverse
}

numbers = []
for _ in range(operations):
    operation, *lines = input().split()
    params = list(map(int, lines))
    functions[operation](numbers, *params)

# https://www.hackerrank.com/challenges/python-tuples/problem

size = int(input())

numbers = tuple(map(int, input().split()))
print(hash(numbers))

# https://www.hackerrank.com/challenges/swap-case/problem


def swap_case(s):
    swap_cased = []
    for char in s:
        if char.islower():
            swap_cased.append(char.upper())
        else:
            swap_cased.append(char.lower())
    return "".join(swap_cased)

# https://www.hackerrank.com/challenges/python-string-split-and-join/problem


def split_and_join(line):
    split = line.split(" ")
    joined = "-".join(split)
    return joined

# https://www.hackerrank.com/challenges/whats-your-name/problem


def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

# https://www.hackerrank.com/challenges/python-mutations/problem


def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

# https://www.hackerrank.com/challenges/find-a-string/problem


def count_substring(string, sub):
    count = 0
    for index in range(len(string)):
        if string[index:].startswith(sub):
            count += 1
    return count

# https://www.hackerrank.com/challenges/string-validators/problem


s = input()

check = [False, False, False, False, False]

for char in s:
    if char.isalnum():
        check[0] = True
    if char.isalpha():
        check[1] = True
    if char.isdigit():
        check[2] = True
    if char.islower():
        check[3] = True
    if char.isupper():
        check[4] = True

print(*check, sep="\n")

# https://www.hackerrank.com/challenges/text-alignment/problem

thickness = int(input())  # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c +
          (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
