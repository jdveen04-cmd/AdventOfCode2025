path = './day4/input.txt'

class Node:
    def __init__(self,x,y,char):
        self.x = x
        self.y = y
        self.char = char

class Grid:
    def __init__(self):
        self.nodes: list[Node] = []
        self.lookup = {}
        self.assembleGrid()
        
    def assembleGrid(self):
        lines = open(path).readlines()
        lines = [line.strip() for line in lines]
        y = 0
        for line in lines:
            x=0
            for char in line:
                node = Node(x,y,char)
                self.nodes.append(node)
                self.lookup[(node.x, node.y)] = node
                x+=1
            y+=1

    def getDirections(self,xRange, yRange):
        directions = set()
        for dx in range(-xRange, xRange + 1):
            for dy in range(-yRange, yRange + 1):
                if (dx, dy) != (0, 0):
                    directions.add((dx, dy))
        return directions

    def getNeighbours(self, node):
        x,y = node.x, node.y
        directions = self.getDirections(1,1)
        neighbourValue = 0
        for dx,dy in directions:
            key = (dx+x, dy+y)
            if key in self.lookup:
                neighbourValue =  neighbourValue + 1 if (self.lookup[key].char) == "@" else neighbourValue+ 0
        return neighbourValue
    
    def getAccesibleNodes(self, value,delete=False):
        accesible = 0
        for node in self.nodes:
            if node.char == ".":
                continue
            if self.getNeighbours(node) < value:
                if(delete):
                    node.char = "."
                accesible += 1
        return(accesible)

def partOne():
    grid = Grid()
    return grid.getAccesibleNodes(4)

def partTwo():
    grid = Grid()
    total = 0
    while True:
        accesible = grid.getAccesibleNodes(4,delete=True)
        if accesible == 0:
            break
        total += accesible
    return total
 
import time
startTime = time.time()
print(f"Part one: {partOne()}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime1 = time.time()
print(f"Part two: {partTwo()}")
print('Execution time part two in seconds: ' + str((time.time() - startTime1)))
print('Execution time both parts: ' + str((time.time() - startTime)))