def getPoints(line):
    currentLocation = (0,0)
    locationsVisited = []
    lineMovements = line.split(',')
    for direction in lineMovements:
        amountToMove = int(direction[1:])
        for _ in range(amountToMove):
            if direction[0] == 'U':
                currentLocation = (currentLocation[0], currentLocation[1]+1)
            if direction[0] == 'D':
                currentLocation = (currentLocation[0], currentLocation[1]-1)
            if direction[0] == 'L':
                currentLocation = (currentLocation[0]-1, currentLocation[1])
            if direction[0] == 'R':
                currentLocation = (currentLocation[0]+1, currentLocation[1])
            locationsVisited.append(currentLocation)
    # return set(sorted(locationsVisited, key=lambda x: abs(x[0])+abs(x[1])))
    return set(locationsVisited)

if __name__ == "__main__":
    with open('inputProblem3.txt') as inputFile:
        line1 = inputFile.readline()
        line2 = inputFile.readline()
    
    firstCross = sorted(getPoints(line1).intersection(getPoints(line2)), key=lambda x: abs(x[0])+abs(x[1]))[0]

    print(firstCross, abs(firstCross[0])+abs(firstCross[1]))
