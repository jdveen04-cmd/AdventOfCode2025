def initGrid():
    lines = open('./data/day4.txt').readlines()
    lines = [line.strip() for line in lines]
    grid = Grid()
    y = 0
    for line in lines:
        x=0
        for char in line:
            node = Node(x,y,char)
            grid.addNode(node)
            x+=1
        y+=1
    return grid

class Node:
    def __init__(self,x,y,char):
        self.x = x
        self.y = y
        self.char = char

class Grid:
    def __init__(self):
        self.nodes: list[Node] = []
        self.lookup = {}

    def addNode(self, node):
        self.nodes.append(node)
        self.lookup[(node.x, node.y)] = node
    
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

def part1():
    grid = initGrid()
    accesible = 0
    for node in grid.nodes:
        if node.char == ".":
            continue
        if grid.getNeighbours(node) < 4:
            accesible += 1
    return(accesible)

def part2():
    grid = initGrid()
    total = 0
    while True:
        accesible = 0
        for node in grid.nodes:
            if node.char == ".":
                continue
            if grid.getNeighbours(node) < 4:
                accesible += 1
                node.char = "."
        if accesible == 0:
            break
        total += accesible
        accesible = 0
    return total

import time
startTime = time.time()
print(f"Part one: {part1()}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime1 = time.time()
print(f"Part two: {part2()}")
print('Execution time part two in seconds: ' + str((time.time() - startTime1)))
print('Execution time both parts: ' + str((time.time() - startTime)))