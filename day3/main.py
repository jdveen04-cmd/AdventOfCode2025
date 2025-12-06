path = './day3/input.txt'

def getHighestNumber(battery,fuelCellsLeft):
    return sorted(battery[:len(battery)-fuelCellsLeft],reverse=True)[0]

def calc(fuelCellAmount):
    lines = [line.rstrip() for line in open(path).readlines()]
    result = 0   
    for line in lines:
        index = 0
        temp = ""
        for fuelCellsLeft in reversed(range(fuelCellAmount)):
            line = line[index:]
            num = getHighestNumber(line,fuelCellsLeft)
            index = line.index(num)+1
            temp += str(num)
        result += int(temp)
    return result

import time
startTime = time.time()
print("part1: ", calc(2))
print(time.time()-startTime)
print("part2: ", calc(12))