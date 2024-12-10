from itertools import product
from operator import mul, add

equations = []

with open("input") as file:
    for line in file:
        equation = line.rstrip().rsplit(":")
        equation[0] = int(equation[0])
        equation[1] = equation[1].strip().split(" ")
        for i in range(len(equation[1])):
            equation[1][i] = int(equation[1][i])
        equations.append(equation)

validValues = []

for equation in equations:
    expectedResult = equation[0]
    operations = product([add, mul], repeat=len(equation[1]) - 1)
    for operation in operations:
        result = 0
        for i in range(len(equation[1]) - 1):
            if i == 0:
                a = equation[1][i]
            else:
                a = result
            b = equation[1][i + 1]
            result = operation[i](a, b)
        if expectedResult == result:
            validValues.append(equation[0])
            break

print(validValues)

total = 0

for value in validValues:
    total += value

print(total)