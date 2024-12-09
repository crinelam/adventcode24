list1 = []
list2 = []

with open("input") as file:
    for line in file:
        #print(line.rstrip())
        lineNums = line.rsplit()
        list1.append(lineNums[0])
        list2.append(lineNums[1])

list1.sort()
list2.sort()

totalDistance = 0

for i in range(len(list1)):
    totalDistance += abs(int(list1[i]) - int(list2[i]))

print(totalDistance)