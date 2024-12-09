wordSearch = []

getIndexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]

with open("input") as file:
    for line in file:
        wordSearch.append(list(line))

indexes = []

for i in range(len(wordSearch)):
    index = getIndexes("A", wordSearch[i])
    for ix in index:
        indexes.append([i, ix])

totalWords = 0

for index in indexes:
    i = index[0]
    j = index[1]
    # Horizontal
    # Diagonal
    if not (i-1 < 0 or j-1 < 0 or i+1 >= len(wordSearch) or j+1 >= len(wordSearch[i]) or i-1 < 0 or j+1 >= len(wordSearch[i]) or i+1 >= len(wordSearch) or j-1 < 0):
        if wordSearch[i-1][j-1] == "M" and wordSearch[i+1][j+1] == "S" and wordSearch[i-1][j+1] == "M" and wordSearch[i+1][j-1] == "S":
            totalWords += 1
        if wordSearch[i-1][j-1] == "S" and wordSearch[i+1][j+1] == "M" and wordSearch[i-1][j+1] == "S" and wordSearch[i+1][j-1] == "M":
            totalWords += 1
        if wordSearch[i-1][j-1] == "M" and wordSearch[i+1][j+1] == "S" and wordSearch[i-1][j+1] == "S" and wordSearch[i+1][j-1] == "M":
            totalWords += 1
        if wordSearch[i-1][j-1] == "S" and wordSearch[i+1][j+1] == "M" and wordSearch[i-1][j+1] == "M" and wordSearch[i+1][j-1] == "S":
            totalWords += 1

print(totalWords)