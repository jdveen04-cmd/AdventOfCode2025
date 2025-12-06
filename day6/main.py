path = './day6/input.txt'

class Day6:
    def __init__(self):
        self.arrays: list[list] = []
        self.reader()
        
    def reader(self):
        lines = [line.rstrip("\n") for line in open(path).readlines()] 
        emptyColumns = self.detectEmptyColumns(lines)
        # divide the line into subparts based on the emptycolumns
        for line in lines:
            array = []
            prev_index = 0
            for empty_index in emptyColumns:
                array.append(line[prev_index:empty_index])
                prev_index = empty_index + 1
            array.append(line[prev_index:])
            self.arrays.append(array)
        # Now redistibute the arrays
        newArray:list[list] = []
        while len(newArray) < len(self.arrays[0]):
            newArray.append([])
        for index in range(len(self.arrays[0])):
            for array in self.arrays:
                newArray[index].append(array[index])
        self.arrays = newArray

    def detectEmptyColumns(self, lines):
        emptyColumns = []
        width = max(len(line) for line in lines)
        for y in range(width):
            if all((line[y] if y < len(line) else " ") == " " for line in lines):
                emptyColumns.append(y)
        return emptyColumns
        
    def convertToCephalopod(self):
        newArrays = []
        for index,array in enumerate(self.arrays):
            length = len(array[0])
            newNumbers = []
            while len(newNumbers) < length:
                newNumbers.append("")
            for index in range(length):
                for number in array[:-1]:
                    newNumbers[index] += number[index]
            newNumbers.append(array[-1])
            newArrays.append(newNumbers)
        self.arrays = newArrays
    
    def calcScore(self):
        total =0
        for array in self.arrays:
            char = array[-1]
            if char.count("*") == 1:
                subtotal = 1
                for number in array[:-1]:
                    subtotal = subtotal * int(number)
                total += subtotal
            elif char.count("+") == 1:
                subtotal = 0
                for number in array[:-1]:
                    subtotal += int(number)
                total += subtotal
        return total

def partOne():
    p1 = Day6()
    return p1.calcScore()

def partTwo():
    p2 = Day6()
    p2.convertToCephalopod()
    return p2.calcScore()

import time
startTime = time.time()
print(f"Part one: {partOne()}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime1 = time.time()
print(f"Part two: {partTwo()}")
print('Execution time part two in seconds: ' + str((time.time() - startTime1)))
print('Execution time both parts: ' + str((time.time() - startTime)))