path = 'adventOfCode2025/day9/input.txt'

class RectangleSolver:
    def __init__(self):
        self.points:list[tuple] = []  # List of (x, y) tuples
        self.segments: list[tuple] = []  # List of polygon edges
        self.max_area = [0,[(0,0),(0,0)]]

    def solvePartOne(self):
        lines = [line.rstrip() for line in open(path).readlines()]
        for line in lines:
            x, y = map(int, line.split(','))
            self.points.append((x, y))
        for point in self.points:
            x1, y1 = point
            for point2 in self.points:
                x2, y2 = point2
                area = (x2 - x1+1) * (y2 - y1+1)
                if area > self.max_area[0]:
                    self.max_area = [area, [(x1,y1),(x2,y2)]]
        return self.max_area

    def solvePartTwo(self):
        lines = [line.rstrip() for line in open(path).readlines()]
        for line in lines:
            x, y = map(int, line.split(','))
            self.points.append((x, y))
        for index,point in enumerate(self.points):
            point2 = self.points[(index+1)%len(self.points)]
            self.segments.append((point, point2))
        for point in self.points:
            x1, y1 = point
            for point2 in self.points:
                x2, y2 = point2
                area = (abs(x2 - x1)+1) * (abs(y2 - y1)+1)
                if not self.validRectangle(point,point2):
                    continue
                if area > self.max_area[0]:
                    self.max_area = [area, [(x1,y1),(x2,y2)]]
        return self.max_area
    
    def validRectangle(self, pointA:tuple, pointB:tuple) -> bool:
        point3 = (pointA[0], pointB[1])
        point4 = (pointB[0], pointA[1])
        if not self.isInside(point3):
            return False
        if not self.isInside(point4):
            return False
        if self.rectangleGetsCut(pointA, pointB):
            return False
        return True
    
    def isInside(self, point:tuple) -> bool:
        inside = False
        x,y = point
        for seg in self.segments:
            if self.isOnSegment(point, seg):
                return True
            (x1,y1), (x2,y2) = seg
            if(x1 != x2):
                continue
            if min(y1,y2) <= y < max(y1,y2):
                if x < x1:
                    inside = not inside
        return inside
    
    def isOnSegment(self, point, segment:tuple) -> bool:
        x,y = point
        (x1,y1), (x2,y2) = segment
        if x1 == x2 == x and min(y1,y2) <= y <= max(y1,y2):
            return True
        if y1 == y2 == y and min(x1,x2) <= x <= max(x1,x2):
            return True
        return False

    def rectangleGetsCut(self, pointA:tuple, pointB:tuple) -> bool:
        xMin,xMax = min(pointA[0], pointB[0]), max(pointA[0], pointB[0])
        yMin,yMax = min(pointA[1], pointB[1]), max(pointA[1], pointB[1])
        for seg in self.segments:
            (x1,y1), (x2,y2) = seg
            if x1 == x2:
                if xMin < x1 < xMax:
                    seg_y_min, seg_y_max = min(y1, y2), max(y1, y2)
                    if max(yMin, seg_y_min) < min(yMax, seg_y_max):
                        return True
            elif y1 == y2:
                if yMin < y1 < yMax:
                    seg_x_min, seg_x_max = min(x1, x2), max(x1, x2)
                    if max(xMin, seg_x_min) < min(xMax, seg_x_max):
                        return True 
        return False

def partOne():
    rs = RectangleSolver()
    return rs.solvePartOne()

def partTwo():
    rs = RectangleSolver()
    return rs.solvePartTwo()

import time
startTime = time.time()
print(f"Part one: {partOne()}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime1 = time.time()
print(f"Part two: {partTwo()}")
print('Execution time part two in seconds: ' + str((time.time() - startTime1)))
print('Execution time both parts: ' + str((time.time() - startTime)))