import re

regex = "mul\(\d+,\d+\)"

input = ""

with open("input") as file:
    for line in file:
        input += line.rstrip()

mults = re.findall(regex, input)

total = 0

for mult in mults:
    mult = mult.replace("mul(", "")
    mult = mult.replace(")", "")
    nums = mult.split(",")
    total += (int(nums[0]) * int(nums[1]))

print(total)