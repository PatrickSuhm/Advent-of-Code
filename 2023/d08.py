import math

f = open("data.txt","r")
lines = f.readlines()

direc = None
maps = {}
for i,l in enumerate(lines):
    l = l.strip()
    if i == 0:
        direc = lines[0].strip()
    if i > 1:
        dest = l.split(" = ")[0]
        left = l.split(" = ")[1].split(", ")[0].replace("(","")
        right = l.split(" = ")[1].split(", ")[1].replace(")","")
        maps[dest]= {"L":left, "R":right}

def findSteps(start, goalEndsWith):
    now = start
    steps = 0
    found = False
    rounds = 0
    while not found:
        rounds += 1
        for di in direc:
            steps += 1
            now = maps[now][di]
            if now.endswith(goalEndsWith):
                found = True
                break
    return steps

print("Part1:",findSteps("AAA", "ZZZ"))

AEndingAr = []
for k in maps:
    if k[2] == "A":
        AEndingAr.append(k)

cycLenAr = []
for ae in AEndingAr:
    now = ae
    steps = 0
    found = False
    trys = 0
    cycLenAr.append(findSteps(ae,"Z"))

print("Part2:",math.lcm(*cycLenAr))
test = 1