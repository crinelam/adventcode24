list1 = []
list2 = []

with open("input") as file:
    for line in file:
        #print(line.rstrip())
        lineNums = line.rsplit()
        list1.append(lineNums[0])
        list2.append(lineNums[1])

totalSimilitude = 0

getIndexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]

for i in range(len(list1)):
    ocurrences = getIndexes(list1[i], list2)
    totalSimilitude += int(list1[i]) * len(ocurrences)

print(totalSimilitude)