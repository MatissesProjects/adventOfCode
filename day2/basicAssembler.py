with open('inputProblem2.txt') as inputFile:
    example = inputFile.readline()
# wanted output 3500

opCodes = example.split(',')

for i in range(0, len(opCodes), 4):
    opCode = opCodes[i]
    if opCode == '99':
        break

    registerToGet1 = int(opCodes[i+1])
    registerToGet2 = int(opCodes[i+2])
    registerToStoreTo = int(opCodes[i+3])

    register1 = int(opCodes[registerToGet1])
    register2 = int(opCodes[registerToGet2])

    # add 1
    if opCode == '1':
        opCodes[registerToStoreTo] = register1 + register2
    # mult 2
    if opCode == '2':
        opCodes[registerToStoreTo] = register1 * register2


print(opCodes[0])