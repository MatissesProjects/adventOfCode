def calcGas(mass):
    return max(int(mass/3) - 2, 0)

if __name__ == "__main__":
    totalGas = 0
    with open('inputProblem1.txt') as inputFile:
        line = inputFile.readline()
        while line:
            totalGas += calcGas(int(line))

            line = inputFile.readline()
    
    print(totalGas)