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
    return locationsVisited

if __name__ == "__main__":
    with open('inputProblem3.txt') as inputFile:
        line1 = inputFile.readline()
        line2 = inputFile.readline()
    line1Points = getPoints(line1)
    line2Points = getPoints(line2)


    crosses = set(line1Points).intersection(set(line2Points))
    print(crosses)

    stepsToCrosses = []
    for cross in crosses:
        distanceToCross1 = line1Points.index(cross) + 1
        distanceToCross2 = line2Points.index(cross) + 1
        stepsToCrosses.append(distanceToCross1 + distanceToCross2)
        
    print(min(stepsToCrosses))
    # print(firstCross, abs(firstCross[0])+abs(firstCross[1]))
