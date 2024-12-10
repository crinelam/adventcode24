from dataclasses import dataclass

map = []

@dataclass
class MapIcons:
    obstacle: str = "#"
    empty: str = "."
    guard: str = "^"
    passed: str = "X"

@dataclass
class Directions:
    up: int = 0
    right: int = 1
    down: int = 2
    left: int = 3

def rotate(direction):
    direction += 1
    if direction > 3:
        direction = 0
    return direction

with open("input") as file:
    for line in file:
        map.append(list(line.rstrip()))

icons = MapIcons()
dirs = Directions()

currentPos = [0, 0]
currentDirection = dirs.up

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == icons.guard:
            currentPos = [i, j]
            break

escaped = False
while not escaped:
    i, j = currentPos
    if currentPos[0] < 0 or currentPos[0] >= len(map) or currentPos[1] < 0 or currentPos[1] >= len(map[0]):
        escaped = True
        break
    map[i][j] = icons.passed
    if currentDirection == dirs.up:
        if i-1 >= 0 and map[i-1][j] is not icons.obstacle:
            currentPos = [i-1, j]
        elif i-1 < 0:
            currentPos = [i-1, j]
        else:
            currentDirection = rotate(currentDirection)
    if currentDirection == dirs.right:
        if j+1 < len(map[i]) and map[i][j+1] is not icons.obstacle:
            currentPos = [i, j+1]
        elif j+1 >= len(map[i]):
            currentPos = [i, j+1]
        else:
            currentDirection = rotate(currentDirection)
    if currentDirection == dirs.down:
        if i+1 < len(map) and map[i+1][j] is not icons.obstacle:
            currentPos = [i+1, j]
        elif i+1 >= len(map):
            currentPos = [i+1, j]
        else:
            currentDirection = rotate(currentDirection)
    if currentDirection == dirs.left:
        if j-1 >= 0 and map[i][j-1] is not icons.obstacle:
            currentPos = [i, j-1]
        elif j-1 < 0:
            currentPos = [i, j-1]
        else:
            currentDirection = rotate(currentDirection)

output = open("output", "w")
for i in range(len(map)):
    for j in range(len(map[i])):
        output.write(map[i][j])
    output.write("\n")
output.close()

totalPassed = 0

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == icons.passed:
            totalPassed += 1

print(totalPassed)