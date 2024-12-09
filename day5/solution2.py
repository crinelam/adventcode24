rules = []
updates = []

with open("input") as file:
    for line in file:
        if "|" in line:
            rules.append(line.rstrip().rsplit("|"))
        elif "," in line:
            updates.append(line.rstrip().rsplit(","))

totalMiddlePages = 0

for update in updates:
    isValid = True
    for rule in rules:
        currentPage = rule[0]
        posteriorPage = rule[1]
        for i in range(len(update)):
            if update[i] == currentPage:
                if posteriorPage in update[:i]:
                    isValid = False
                    break

    if not isValid:
        while not isValid:
            isValid = True
            for rule in rules:
                currentPage = rule[0]
                posteriorPage = rule[1]
                for i in range(len(update)):
                    if update[i] == currentPage:
                        if posteriorPage in update[:i]:
                            posteriorPageIdx = update.index(posteriorPage)
                            posteriorPageVal = update.pop(posteriorPageIdx)
                            update.insert(i, posteriorPageVal)
                            isValid = False
                            break
        totalMiddlePages += int(update[len(update)//2])


print(totalMiddlePages)