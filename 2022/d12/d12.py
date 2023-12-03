lines = open("data.txt", "r").readlines()

class MyMap:
    def __init__(s, inp):
        s.data = []
        s.start = (-1, -1)    # (x,y)
        s.goal = (-1, -1)
        s.aList = []
        d = []
        y,x = 0,0
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for l in inp:
            for c in l:
                if c == "S":
                    d.append(0)
                    s.start = (x, y)
                elif c == "E":
                    d.append(25)
                    s.goal = (x, y)
                elif c == "\n":
                    s.data.append(d)
                    d = []
                else:
                    d.append(alpha.find(c))
                    if c == "a":
                        s.aList.append((x,y))
                x += 1
            x = 0
            y += 1
        s.maxY = len(s.data)-1
        s.maxX = len(s.data[0])-1

    def getEle(s,pos):
        return(s.data[pos[1]][pos[0]])
        
mm = MyMap(lines)
fnl = []
myGraph = {}

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
for y in range(mm.maxY+1):
    for x in range(mm.maxX+1):                              # go over all locations in the map
        for dir in dirs:
            dx,dy = dir[0],dir[1]
            if x+dx >= 0 and x+dx <= mm.maxX:
                if y+dy >= 0 and y+dy <= mm.maxY:
                    if mm.getEle((x+dx,y+dy)) <= mm.getEle((x,y))+1: # at most 1 higher
                        fnl.append((x+dx,y+dy))             # store every feasible neigbor of current loc in a list
        myGraph[str((x,y))] = fnl
        fnl = []

minDist = 1e9
for part in [1,2]:
    if part == 1: startList = [mm.start]        # Part 1 starts at S
    else: startList = mm.aList                  # Part 2 starts at every a and finds minimum steps
    for start in startList:
        # BFS works because graph is not weighted
        visited = [start]
        queue = [start]
        dists = {str(start):0}
        while queue:
            key = queue.pop(0) 
            for child in myGraph[str(key)]:
                if child not in visited:
                    visited.append(child)
                    queue.append(child)
                    dists[str(child)] = dists[str(key)] + 1
        if str(mm.goal) in dists:
            if dists[str(mm.goal)] < minDist:
                minDist = dists[str(mm.goal)]

    print("Part",str(part)+":", minDist)

                

