import copy

f = open("data.txt","r")
lines = f.readlines()

oris = []
for line in lines:
    dat = line.strip().split()
    oris.append(dat)
for i,ori in enumerate(oris):
    intVals = []
    for o in ori:
        intVals.append(int(o))
    oris[i] = intVals
            

def difAr(inpAr):
    dif = []
    for j,inti in enumerate(inpAr):
        if j > 0:
            dif.append(inpAr[j]-inpAr[j-1])
    return dif

def part1():
    lasts = []
    for ori in oris:

        diffed = [copy.deepcopy(ori)]
        while not all(elem == 0 for elem in diffed[-1]):
            diffed.append(difAr(diffed[-1]))
        
        le = len(diffed)
        for ii,diff in enumerate(diffed):
            i = le-ii-1
            if i == le-1:
                diffed[i].append(0)
            else:
                diffed[i].append(diffed[i][-1]+diffed[i+1][-1])

        lasts.append(diffed[0][-1])
    print("Part1:",sum(lasts))

def part2():
    firsts = []
    for ori in oris:

        diffed = [copy.deepcopy(ori)]
        while not all(elem == 0 for elem in diffed[-1]):
            diffed.append(difAr(diffed[-1]))
        
        le = len(diffed)
        for ii,diff in enumerate(diffed):
            i = le-ii-1
            if i == le-1:
                diffed[i].insert(0,0)
            else:
                diffed[i].insert(0, diffed[i][0]-diffed[i+1][0])

        firsts.append(diffed[0][0])
    print("Part2:",sum(firsts))

part1()
part2()