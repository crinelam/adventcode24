wordSearch = []

getIndexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]

with open("input") as file:
    for line in file:
        wordSearch.append(list(line))

indexes = []

for i in range(len(wordSearch)):
    index = getIndexes("X", wordSearch[i])
    for ix in index:
        indexes.append([i, ix])

totalWords = 0

for index in indexes:
    i = index[0]
    j = index[1]
    # Horizontal
    if not (i-3 < 0):
        if wordSearch[i-1][j] == "M" and wordSearch[i-2][j] == "A" and wordSearch[i-3][j] == "S":
            totalWords += 1
    if not (i+3 >= len(wordSearch)):
        if wordSearch[i+1][j] == "M" and wordSearch[i+2][j] == "A" and wordSearch[i+3][j] == "S":
            totalWords += 1
    # Vertical
    if not (j-3 < 0):
        if wordSearch[i][j-1] == "M" and wordSearch[i][j-2] == "A" and wordSearch[i][j-3] == "S":
            totalWords += 1
    if not (j+3 >= len(wordSearch[i])):
        if wordSearch[i][j+1] == "M" and wordSearch[i][j+2] == "A" and wordSearch[i][j+3] == "S":
            totalWords += 1
    # Diagonal
    if not (i-3 < 0 or j-3 < 0):
        if wordSearch[i-1][j-1] == "M" and wordSearch[i-2][j-2] == "A" and wordSearch[i-3][j-3] == "S":
            totalWords += 1
    if not (i-3 < 0 or j+3 >= len(wordSearch[i])):
        if wordSearch[i-1][j+1] == "M" and wordSearch[i-2][j+2] == "A" and wordSearch[i-3][j+3] == "S":
            totalWords += 1
    if not (i+3 >= len(wordSearch) or j-3 < 0):
        if wordSearch[i+1][j-1] == "M" and wordSearch[i+2][j-2] == "A" and wordSearch[i+3][j-3] == "S":
            totalWords += 1
    if not (i+3 >= len(wordSearch) or j+3 >= len(wordSearch[i])):
        if wordSearch[i+1][j+1] == "M" and wordSearch[i+2][j+2] == "A" and wordSearch[i+3][j+3] == "S":
            totalWords += 1

print(totalWords)