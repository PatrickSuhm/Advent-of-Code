import sys
sys.setrecursionlimit(10**5)

f = open("data.txt","r")
lines = [line.strip() for line in f.readlines()]

def insideBorder(coo):
    y,x = coo
    if (y >= 0 and y < len(lines) and 
        x >= 0 and x < len(lines[0])):
        return True
    return False

def getChar(coo):
    if insideBorder(coo):
        return lines[coo[0]][coo[1]]
    return ""

def getNewCoo(coo, dir):
    y,x = coo
    if dir == "right":
        return (y, x+1)
    if dir == "up":
        return (y-1, x)
    if dir == "left":
        return (y, x-1)
    if dir == "down":
        return(y+1, x)

def addTiles(coo,dir):
    global cooSet

    c = getChar(coo)
    
    if c == "":
        return

    if (coo[0],coo[1],dir) in cooSet:
        return
    
    cooSet.add((coo[0],coo[1],dir))
    #print((coo[0],coo[1],dir))

    if c == ".":
       addTiles(getNewCoo(coo,dir), dir)

    elif c == "|":
        if dir in ["right","left"]:
            addTiles(getNewCoo(coo,"up"),"up")
            addTiles(getNewCoo(coo,"down"),"down")
        if dir in ["up","down"]:
            addTiles(getNewCoo(coo,dir),dir)        
    
    elif c == "-":
        if dir in ["up","down"]:
            addTiles(getNewCoo(coo,"right"),"right")
            addTiles(getNewCoo(coo,"left"),"left")
        if dir in ["left","right"]:
            addTiles(getNewCoo(coo,dir),dir)         
    
    elif c == "\\":
        if dir == "right":
            addTiles(getNewCoo(coo,"down"),"down")
        if dir == "up":
            addTiles(getNewCoo(coo,"left"),"left")
        if dir == "down":
            addTiles(getNewCoo(coo,"right"),"right")
        if dir == "left":
            addTiles(getNewCoo(coo,"up"),"up")

    elif c == "/":
        if dir == "right":
            addTiles(getNewCoo(coo,"up"),"up")
        if dir == "up":
            addTiles(getNewCoo(coo,"right"),"right")
        if dir == "down":
            addTiles(getNewCoo(coo,"left"),"left")
        if dir == "left":
            addTiles(getNewCoo(coo,"down"),"down")
    else:
        assert False, "dont arrive here!"

def getStartList():
    startList = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if x == 0:
                startList.append([y,x,"right"])
            if y == 0:
                startList.append([y,x,"down"])
            if x == len(lines[0])-1:
                startList.append([y,x,"left"])
            if y == len(lines)-1:
                startList.append([y,x,"up"])
    return startList

for part in ["1","2"]:
    maxTiles = 0
    if part == "2":
        startList = getStartList()
    else: startList = [[0,0,"right"]]
    for start in startList:
        cooSet = set()
        addTiles((start[0], start[1]), start[2])
        uniqueCoo = set()
        for c in cooSet:
            uniqueCoo.add((c[0],c[1]))
        maxTiles = max(maxTiles, len(uniqueCoo))
    print("Part"+part+":",maxTiles)

