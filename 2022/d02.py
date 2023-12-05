
lines = open("data.txt", "r").readlines()
d = {"A":"R", "B":"P", "C":"S", "X":"R", "Y":"P", "Z":"S"}

def addScore(score):
    points = {"R":1, "P":2, "S":3}
    winList = ["RP", "PS", "SR"]
    looseList = ["PR", "SP", "RS"]
    loosP = 0
    drawP = 3
    winP = 6
    if op == me:
        score += drawP + points[me]
    elif op+me in winList:
        score += winP + points[me]
    elif op+me in looseList:
        score += loosP + points[me]
    return score

def getMyChoice(op, outcome):
    loosDic = {"R":"S", "P":"R", "S":"P"}
    winDic = {"R":"P", "P":"S", "S":"R"}
    if outcome == "X":
        return loosDic[op]
    if outcome == "Y":
        return op
    if outcome == "Z":
        return winDic[op]

#--- Part 1
score = 0
for l in lines:
    l = l.split()
    op = d[l[0]]
    me = d[l[1]]
    score = addScore(score)
print("Part 1:", score)

#--- Part 2
score = 0
for l in lines:
    l = l.split()
    op = d[l[0]]
    me = getMyChoice(op, l[1])
    score = addScore(score)
print("Part 2:", score)



