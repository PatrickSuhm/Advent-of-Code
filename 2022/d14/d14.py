import numpy as np
lines = open("data.txt", "r").readlines()

data = [[(int(d.split(",")[0]), int(d.split(",")[1])) for d in l.split(" -> ")] for l in lines]

class Pg:
    def __init__(s, data, part, start = (500,0)):
        s.start = start
        s.part = part
        s.bX = (start[0], start[0])
        s.bY = (start[1], start[1])
        for l in data:
            for coord in l:
                s.bX = (min(s.bX[0], coord[0]), max(s.bX[1], coord[0]))
                s.bY = (min(s.bY[0], coord[1]), max(s.bY[1], coord[1]))
        
        if s.part == 2:
            s.bY = (s.bY[0], s.bY[1] + 2)
            s.bX = (s.bX[0]-1000, s.bX[1]+1000)

        s.pg = []
        for y in range(0, s.bY[1]+1):
            s.pg.append([])
            for x in range(0, s.bX[1]-s.bX[0]+1):
                s.pg[y].append(".")

        for l in data:
            for i,cp in enumerate(l[:-1]):
                xStart, xEnd = min(cp[0], l[i+1][0]), max(cp[0], l[i+1][0])
                yStart, yEnd = min(cp[1], l[i+1][1]), max(cp[1], l[i+1][1])
                for x in range(xStart, xEnd+1):
                    for y in range(yStart, yEnd+1):
                        s.pg[y][x-s.bX[0]] = "#"  
        
        if part == 2:
            for x in range(0, s.bX[1]-s.bX[0]+1):
                s.pg[s.bY[1]][x] = "#"  


    def print(s):
        for i in range(len(s.pg)):
            print("".join(s.pg[i]))

    def getStart(s):
        return s.start

    def isValid(s, coord):
        if s.part == 1:
            if (coord[0] >= s.bX[0] and coord[0]<= s.bX[1] and
                coord[1] >= s.bY[0] and coord[1]<= s.bY[1]):
                return True
            return False
        if s.part == 2:
            for c in [(s.start[0], s.start[1]+1), (s.start[0]-1, s.start[1]+1), (s.start[0]+1, s.start[1]+1)]:
                if s.isFree(c):
                    return True
            return False
        
    
    def isFree(s, coord):
        if s.pg[coord[1]][coord[0]-s.bX[0]] != ".":
            return False
        return True

    def processCoord(s, coord):
        co = [(coord[0], coord[1]+1), (coord[0]-1, coord[1]+1), (coord[0]+1, coord[1]+1)]
        for c in co:
            if not s.isValid(c):  # stop Program
                return False               
            elif s.isFree(c):
                return s.processCoord(c)

        s.pg[coord[1]][coord[0]-s.bX[0]] = "o"
        return True

for part in range(1,3):
    myPg = Pg(data, part)

    if part == 2: units = 1
    else: units = 0

    while True:
        if not myPg.processCoord(myPg.getStart()):
            break
        #myPg.print() 
        units += 1

       
    print("Part "+str(part)+":",units)


test = 1

    