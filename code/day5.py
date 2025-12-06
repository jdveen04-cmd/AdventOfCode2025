class Range:
    def __init__(self, begin:int, end:int):
        self.begin = int(begin)
        self.end = int(end)
    def __repr__(self):
        return(f"Range from {self.begin} to {self.end}")
    def span(self):
        return self.end-self.begin+1 #because it is inclusive
    def __lt__(self,other):
        return self.begin < other.begin

class dataBase:
    def __init__(self):
        lines = open('./data/day5.txt').readlines()
        self.ranges: list[Range] = []
        self.IDs: list[int] = []
        self.safeItems = set()
        self.read(lines)

    def read(self,lines: list[str]):
        rangeBool= True
        for line in lines:
            if line == "\n":
                rangeBool = False
                self.handleRanges()
                continue
            if rangeBool:
                begin, end = line.split("-")
                self.ranges.append(Range(begin, end))
            elif not rangeBool:
                self.IDs.append(int(line.rstrip()))    

    def handleRanges(self):
        self.ranges = sorted(self.ranges)
        newRanges = [self.ranges[0]]
        for range in self.ranges[1:]:
            previousRange = newRanges[-1]
            if range.begin <= previousRange.end:
                previousRange.end = max(range.end,previousRange.end)
            else:
                newRanges.append(range)
        self.ranges = newRanges

    def checkItems(self):
        for item in self.IDs:
            for range in self.ranges:
                if (range.begin <= item <= range.end):
                    self.safeItems.add(item)
                    break
        return len(self.safeItems)
    
    def countRanges(self):
        totalRanges = 0
        for range in self.ranges:
            totalRanges += range.span()
        return totalRanges
    
def part1():
    db = dataBase()
    return db.checkItems()

def part2():
    db = dataBase()
    return db.countRanges()

import time
startTime = time.time()
print(f"Part one: {part1()}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime1 = time.time()
print(f"Part two: {part2()}")
print('Execution time part two in seconds: ' + str((time.time() - startTime1)))
print('Execution time both parts: ' + str((time.time() - startTime)))