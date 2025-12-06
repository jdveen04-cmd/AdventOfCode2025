line = open("./day2/input.txt").readline()
line = line.rstrip()

ranges = [
    tuple(map(int, r.split("-")))
    for r in line.split(",")
]
def partOne(ranges):
    total = 0
    for entry in ranges:
        begin, end = entry
        digits = len(str(begin))
        if digits % 2 == 1:
            begin = 10 ** (digits)
        sequence = str(begin)[:int(len(str((begin)))/2)]
        while(True):
            word = sequence * 2
            if(int(word)<begin):
                sequence = str(int(sequence) + 1)
                continue
            if(int(word)>end):
                break
            total += int(word)
            sequence = str(int(sequence) + 1)
    return(total)

def part1(ranges):
    total = 0
    for entry in ranges:
        begin, end = entry
        digits = len(str(begin))
        if digits % 2 == 1:
            begin = 10 ** (digits)
        sequence = str(begin)[:int(len(str((begin)))/2)]
        while(True):
            word = sequence * 2
            if(int(word)<begin):
                sequence = str(int(sequence) + 1)
                continue
            if(int(word)>end):
                break
            total += int(word)
            sequence = str(int(sequence) + 1)
    return(total)

def partTwo(ranges):
    total = 0
    for entry in ranges:
        begin,end = entry[0],entry[1]
        for currentNumber in range(begin,end+1):
            for partitionLength in range(1,len(str(currentNumber))):
                if len(str(currentNumber)) % partitionLength != 0: continue
                part = str(currentNumber)[:partitionLength]
                word = part * int((len(str(currentNumber))/partitionLength))
                if (int(word) == currentNumber and (int(word) >= begin) and (int(word) <= end)): 
                    total += currentNumber
                    break
    return total

import time
startTime = time.time()
print(f"Part one: {partOne(ranges)}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime = time.time()
print(f"Part one: {partTwo(ranges)}")
print('Execution time part two in seconds: ' + str((time.time() - startTime)))
