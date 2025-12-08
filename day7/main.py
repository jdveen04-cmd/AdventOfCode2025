path = 'adventOfCode2025/day7/input.txt'

class Laser:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value #number of ways to reach this point
    
    def __repr__(self):
        return f"Laser({self.x}, {self.y}, {self.value})\n"

class LaserTree:
    def __init__(self):
        self.lookup:dict[tuple,Laser] = {}
        self.level: dict[int,list[Laser]] = {}
        self.splits = 0
        self.startLasers()
    
    def startLasers(self):
        lines = [line.rstrip() for line in open(path).readlines()]
        xindex = list(lines[0]).index("S") #find the starting point
        self.addLaser(xindex, 0, 1) #start with one laser at the starting point

        for yindex, line in enumerate(lines[1:], start=1):
            for laser in self.level.get(yindex-1):
                self.handleLine(line,yindex,laser) #Itterate over all lasers in the previous level and extend them downwards
                
    def handleLine(self, line, yindex,laser: Laser):
        if line[laser.x] == ".":
            self.addLaser(laser.x, yindex, laser.value)
        if line[laser.x] == "^":
            self.splits += 1
            if laser.x -1 >= 0 and line[laser.x -1] == ".":
                self.addLaser(laser.x -1, yindex, laser.value)
            if laser.x +1 < len(line) and line[laser.x +1] == ".":
                self.addLaser(laser.x +1, yindex, laser.value)
        
    def addLaser(self, xindex, yindex, laserValue):
            if self.lookup.get((xindex, yindex)) is not None:
                self.lookup.get((xindex, yindex)).value += laserValue
                return
            newLaser = Laser(xindex, yindex, laserValue)
            self.lookup[(xindex, yindex)] = newLaser
            if yindex not in self.level.keys():
                self.level[yindex] = []
            self.level.get(yindex).append(newLaser)

def partOne():
    lt = LaserTree()
    return lt.splits

def partTwo():
    total = 0
    lt = LaserTree()
    for laser in lt.level.get(max(lt.level.keys())):
        total += laser.value
    return total

import time
startTime = time.time()
print(f"Part one: {partOne()}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime1 = time.time()
print(f"Part two: {partTwo()}")
print('Execution time part two in seconds: ' + str((time.time() - startTime1)))
print('Execution time both parts: ' + str((time.time() - startTime)))