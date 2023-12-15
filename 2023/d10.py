import sys
sys.setrecursionlimit(int(1e5))

f = open("data.txt","r")
lines = [line.strip() for line in f.readlines()]

def insideBorder(coo):
    if (coo[0] >= 0 and coo[0] < len(lines) and 
        coo[1] >= 0 and coo[1] < len(lines[0])):
        return True
    return False

def getNeighbors(coo):
    right = (coo[0], coo[1]+1)
    up = (coo[0]-1, coo[1])
    left = (coo[0], coo[1]-1)
    down = (coo[0]+1, coo[1])
    return [right, up, left, down]

def getChar(coo):
    if insideBorder(coo):
        c = lines[coo[0]][coo[1]]
        if c != ".":
            return c
        return -1 
    return -1

def getDir(oldCoo, coo):
    dif = (coo[0] - oldCoo[0],coo[1] - oldCoo[1]) 
    if dif[0] < 0:
        return "up"
    if dif[0] > 0:
        return "down"
    if dif[1] > 0:
        return "right"
    if dif[1] < 0: 
        return "left"
    assert False, "invalid dir"

def getGoing():
    for li,line in enumerate(lines):
        for ci,char in enumerate(line):
            if char == "S":
                start = (li,ci)
                neig = getNeighbors(start)
                possiDir = []

                possibleNeig = []
                for n in neig:
                    c = getChar(n)
                    direc = getDir(start, n)
                    if c != -1: 
                        if ((direc == "up" and c in ["|", "F", "7"]) or
                            (direc == "down" and c in ["|", "J", "L"]) or
                            (direc == "left" and c in ["-","L", "F"]) or
                            (direc == "right" and c in ["-","J","7"])
                            ):
                            possiDir.append(direc)
                            possibleNeig.append(n)
                if "up" in possiDir and "down" in possiDir:
                    startCharIs = "|"
                if "left" in possiDir and "right" in possiDir:
                    startCharIs = "-"
                if "up" == possiDir[0] and "left" == possiDir[1]:
                    startCharIs = "J"
                if "right" == possiDir[0] and "down" == possiDir[1]:
                    startCharIs = "F"
                if "right" == possiDir[0] and "up" == possiDir[1]:
                    startCharIs = "L"
                if "left" == possiDir[0] and "down" == possiDir[1]:
                    startCharIs = "7"

                return start, possibleNeig[0], startCharIs

loopCooList = []
def findNext(oldCoo, coo, dist):
    dist += 1
    c = getChar(coo)
    if c == "S":
        return dist
    if c == "|":
        if getDir(oldCoo, coo) == "up": newCoo = (coo[0]-1, coo[1])
        else: newCoo = (coo[0]+1, coo[1])
    if c == "-":
        if getDir(oldCoo, coo) == "right": newCoo = (coo[0], coo[1]+1)
        else: newCoo = (coo[0], coo[1]-1)
    if c == "L":
        if getDir(oldCoo, coo) == "down": newCoo = (coo[0], coo[1]+1)
        else: newCoo = (coo[0]-1, coo[1])
    if c == "J":
        if getDir(oldCoo, coo) == "right": newCoo = (coo[0]-1, coo[1])
        else: newCoo = (coo[0], coo[1]-1)
    if c == "7":
        if getDir(oldCoo, coo) == "right": newCoo = (coo[0]+1, coo[1])
        else: newCoo = (coo[0], coo[1]-1)
    if c == "F":
        if getDir(oldCoo, coo) == "left": newCoo = (coo[0]+1, coo[1])
        else: newCoo = (coo[0], coo[1]+1)
    
    loopCooList.append(newCoo)
    return findNext(coo, newCoo, dist)

def getlenth():
    start, coo, startCharIs = getGoing()
    loopCooList.append(start)
    loopCooList.append(coo)
    return findNext(start, coo, 0), startCharIs
plen, startCharIs = getlenth()
print("Part1:",int(plen/2))

newLines = [] 
for li,line in enumerate(lines):
    newLine = ""
    for ci,char in enumerate(line.strip()):
        if char == "S":
            newLine+=startCharIs
        else:
            if (li,ci) in loopCooList:
                newLine += char
            else:
                newLine += "."
    newLine.replace("S",startCharIs)
    newLines.append(newLine)
lines = newLines

def getCrossingsRight(coo):
    crossingCnt = 0
    for ci in range(coo[1]+1,len(lines[0])):
        char = lines[coo[0]][ci]
        if char in ["L","J","|"]:
            crossingCnt += 1
    return crossingCnt

coList = []
for li,line in enumerate(lines):
    if li > 0 and li < len(lines):
        for ci,char in enumerate(line.strip()):
            if ci > 0 and ci < len(line)-1:
                if char == ".":
                    numCros = getCrossingsRight((li,ci))
                    if numCros%2 != 0:
                        coList.append((li,ci))  

print("Part2:",len(coList))

test = 1