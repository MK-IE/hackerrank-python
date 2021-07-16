# https://www.hackerrank.com/challenges/write-a-function/problem

def isLeap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


year = int(input())
print(isLeap(year))

# https://www.hackerrank.com/challenges/python-quest-1/problem

# More than 2 lines will result in 0 score. Do not leave a blank line also
for i in range(1, int(input())):
    print([1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999][i - 1])
