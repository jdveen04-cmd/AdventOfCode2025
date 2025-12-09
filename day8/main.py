path = 'adventOfCode2025/day8/input.txt'
class Box:
    def __init__(self, x:int, y:int, z:int):
        self.x = x
        self.y = y
        self.z = z
        self.parent = self
        self.children: list["Box"] = [self]
        self.inJunction = False
    def length(self):
        return len(self.children)
    def __repr__(self):
        return f"Box({self.x}, {self.y}, {self.z}, {self.length()})\n"

class JunctionBoxes:
    def __init__(self):
        self.boxes = []
        self.distances = []
        self.junctions = []
        self.readInput()

    def readInput(self):
        lines = [line.rstrip() for line in open(path).readlines()]
        for line in lines:
            dimensions = line.split(",")
            newBox = Box(int(dimensions[0]), int(dimensions[1]), int(dimensions[2]))
            self.calculateDistances(newBox)
            self.boxes.append(newBox)
        self.distances.sort(key=lambda x: x[0])

    def calculateDistances(self,nBox:Box):
        for box in self.boxes:
            distance = abs(box.x - nBox.x)**2 + abs(box.y - nBox.y)**2 + abs(box.z - nBox.z)**2
            self.distances.append((distance, box, nBox))
    
    def mergeJunctions(self, boxA:Box, boxB:Box):
        parentB = boxB.parent
        parentA = boxA.parent
        for child in parentB.children:
            child.parent = parentA
            parentA.children.append(child)
        parentB.children = [] 
        if parentB in self.junctions:
            self.junctions.remove(parentB)

    def connectBoxes(self, connectionAmount:int,partTwo:bool=False):
        limit = min(connectionAmount, len(self.distances))
        for i in range(limit):
            boxA: Box
            boxB: Box 
            dist,boxA, boxB = self.distances[i]
            if boxA.inJunction and boxB.inJunction:
                if boxA.parent == boxB.parent:
                    continue
                self.mergeJunctions(boxA, boxB)
            elif boxA.inJunction:
                boxB.inJunction = True
                boxB.parent = boxA.parent
                boxA.parent.children.append(boxB)
            elif boxB.inJunction:
                boxA.inJunction = True
                boxA.parent = boxB.parent
                boxB.parent.children.append(boxA)
            else:
                boxA.inJunction = True
                boxB.inJunction = True
                boxB.parent = boxA
                boxA.children.append(boxB)
                self.junctions.append(boxA)
            if partTwo and len(self.junctions) and self.junctions[0].length() == len(self.boxes):
                return boxA.x * boxB.x

        # return the 3 biggest circuits
        self.junctions.sort(key=lambda x: x.length(), reverse=True)
        return self.junctions[0].length() * self.junctions[1].length() * self.junctions[2].length()

def partOne():
    jb = JunctionBoxes()
    return jb.connectBoxes(1000)

def partTwo():
    jb = JunctionBoxes()
    return jb.connectBoxes(len(jb.distances), partTwo = True)

import time
startTime = time.time()
print(f"Part one: {partOne()}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime1 = time.time()
print(f"Part two: {partTwo()}")
print('Execution time part two in seconds: ' + str((time.time() - startTime1)))
print('Execution time both parts: ' + str((time.time() - startTime)))