f = open("data.txt","r")
lines = [[c for c in line.strip()] for line in f.readlines()]

def getHighestPos(x,y):
    global lines
    if y == 0:
        return 0
    if lines[y-1][x] == ".":
        return getHighestPos(x,y-1)
    return y

def tilt():
    global lines
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "O":
                hy = getHighestPos(x,y)
                if hy != y:
                    lines[y][x] = "."
                    lines[hy][x] = "O"

def rotateCW():
    global lines
    rows, cols = len(lines), len(lines[0])
    rotated = [[""] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            rotated[j][rows-1-i] = lines[i][j]
    lines = rotated

def cycle():
    for _ in range(4):
        tilt()
        rotateCW()

for part in [1,2]:
    if part == 1:
        tilt()
    else:
        cycLen = -1
        tu = tuple(tuple(l) for l in lines)
        ar = [tu]
        for i in range(1,int(1e9)+1):
            cycle()
            tu = tuple(tuple(l) for l in lines)
            if tu in ar:
                cycLen = i - ar.index(tu)
                break
            ar.append(tu)
        inCycIdx = (int(1e9)-ar.index(tu))%cycLen + ar.index(tu)
        lines = ar[inCycIdx]

    cnts = [l.count("O") for l in lines]
    total = 0
    for i,c in enumerate(cnts):
        total += (len(cnts)-i)*c

    print("Part"+str(part)+":",total)