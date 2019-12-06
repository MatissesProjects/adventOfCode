# puzzleInput = 109165-576723

# to brute force we need
# start at bottom of range, check against each rule, add to list if passes


# rules
# 6 digit
# requires a double
# must be monotonically increasing

goodPasswordList = []
for num in range(109165, 576724):
    strNum = str(num)
    if(strNum[0] <= strNum[1] <= strNum[2] <= strNum[3] <= strNum[4] <= strNum[5]):
        if(strNum[0] == strNum[1] or strNum[1] == strNum[2] or
           strNum[2] == strNum[3] or strNum[3] == strNum[4] or
           strNum[4] == strNum[5]):
            goodPasswordList.append(num)
        
print(len(goodPasswordList))
