f = open("data.txt","r")
lines = [line.strip().split(" ") for line in f.readlines()]

def unfoldPat(pat):
    unfolded = pat
    for _ in range(4):
        unfolded += "?"+pat
    return unfolded

import copy 
def unfoldGr(gr):
    unfolded = copy.deepcopy(gr)
    for _ in range(4):
        unfolded+=gr
    return unfolded

def shortPattern(pat):
    shortPattern, old = "", ""
    for char in pat:
        if char == ".":
            if old != ".":
                shortPattern += char
            old = "."
        else:
            shortPattern += char
            old = char
    shortPattern = shortPattern.strip(".")
    return shortPattern

cache = {}
def getVaris(pattern, groupes):

    key = (pattern, groupes)
    if key in cache:
        return cache[key] 

    varis = 0

    if pattern == "": 
        if groupes == ():
            cache[key] = 1
            return 1 
        cache[key] = 0
        return 0
    
    if groupes == ():
        if "#" in pattern:
            cache[key] = 0
            return 0
        cache[key] = 1
        return 1
    
    if pattern[0] in ["?","."]:
        varis += getVaris(pattern[1:],groupes)

    if pattern[0] in ["?","#"]:
        if groupes[0] <= len(pattern):
            if "." not in pattern[:groupes[0]]: 
                if groupes[0] == len(pattern) or pattern[groupes[0]] != "#":
                    varis += getVaris(pattern[groupes[0]+1:], groupes[1:])

    cache[key] = varis
    return varis

for part in [1,2]:
    totalVaris = 0
    for i,line in enumerate(lines):
        pattern = line[0]
        if part == 2: pattern = unfoldPat(pattern)
        pattern = shortPattern(pattern)
        groupes = tuple([int(l) for l in line[1].split(",")])
        if part == 2: groupes = unfoldGr(groupes)
        totalVaris += getVaris(pattern, groupes)
    print("Part"+str(part)+":",totalVaris)
