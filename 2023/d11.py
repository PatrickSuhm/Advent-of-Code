import sys
sys.setrecursionlimit(int(1e5))

f = open("data.txt","r")
lines = [line.strip() for line in f.readlines()]
expanded1 = []
rowIdx = []
for i,line in enumerate(lines):
    if line.endswith("."*(len(line))):
        expanded1.append(line)
        rowIdx.append(i)
    expanded1.append(line)
colIdx = []
for i in range(len(lines[0])):    
    col = ""
    for line in lines:
        col+=line[i]
    if col.endswith("."*(len(col))):
        colIdx.append(i)
expanded = []
for l in expanded1:
    newL = []
    for i,c in enumerate(l):
        if i in colIdx:
            newL.append(".")
        newL.append(c)
    expanded.append(newL)
cnt = 0
gala = []
for li,line in enumerate(expanded):
    for ci,char in enumerate(line):
        if char == "#":
            expanded[li][ci] = str(cnt)
            gala.append([li, ci])

def getDist(ga1,ga2):
    return abs(ga2[0]-ga1[0])+abs(ga2[1]-ga1[1])

def getDist2(rowIdx,colIdx,ga1,ga2):
    r1 = ga2[0]
    r2 = ga1[0]
    c1 = ga2[1]
    c2 = ga1[1]
    rowDist = abs(r1-r2)
    colDist = abs(c1-c2)
    for r in rowIdx:
        if (r < r1 and r > r2 or 
            r > r1 and r < r2):
            rowDist += 10-2
    for c in colIdx:
        if (c < c1 and c > c2 or 
            c > c1 and c < c2):
            colDist += 10-2

    return rowDist+colDist

distSum1 = 0
distSum2 = 0
for i in range(0,len(gala)):
    for j in range(i,len(gala)):
        distSum1 += getDist(gala[i],gala[j])
        distSum2 += getDist2(rowIdx, colIdx, gala[i],gala[j])
print("Part1:",distSum1)
print("Part2:",distSum2)
test = 1
