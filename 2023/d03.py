f = open("data.txt","r")
lines = f.readlines()

def getNumsFromLine(line):
    current = ""
    numbers = []
    start = None
    for i, char in enumerate(line):
        if char.isdigit():
            if start is None:
                start = i
            current += char
        elif current:
            end = i - 1
            numbers.append({
                "value": int(current),
                "start": start,
                "end": end
            })
            current = ""
            start = None
    if current:
        end = len(line) - 1
        numbers.append({
            "value": int(current),
            "start": start,
            "end": end
        })
    return numbers

def isSpecialSym(val):
    if val == ".":
        return False
    if not val.isdigit():
        return True
    return False

def checkIdx(idx, lineAbove, line, lineBelow):

    left = max(0,idx-1)
    center = idx
    right = min(len(line)-1,idx+1)
    idxToCheck=[left,center,right]
    for i in idxToCheck:
        if lineAbove != "":
            if isSpecialSym(lineAbove[i]):
                return True
        
        if isSpecialSym(line[i]):
            return True
        
        if lineBelow != "":
            if isSpecialSym(lineBelow[i]):
                return True

    return False

def isNumInAr(arr, num):
    for a in arr:
        if (a["value"] == num["value"] and 
            a["start"] == num["start"] and 
            a["end"] == num["end"]):
            return True
    return False

numAr = []
def addToPartNrAr(lineAbove, line, lineBelow):
    numsInLine = getNumsFromLine(line)
    locNumAr = []
    for num in numsInLine:
        for idx in range(num["start"], num["end"]+1):
            if checkIdx(idx, lineAbove, line, lineBelow):
                if not isNumInAr(locNumAr, num):
                    locNumAr.append(num)
    for nu in locNumAr:
        numAr.append(nu["value"])

##----------------------------------------------------
def getIdxFromStar(line):
    idxAr = []
    for i,char in enumerate(line):
        if char == "*":
            idxAr.append(i)
    return idxAr

def getAdjUniqueNumSum(idx,line,lineAbove,lineBelow):
    
    numsAbove = getNumsFromLine(lineAbove) if lineAbove != "" else []
    nums = getNumsFromLine(line)
    numsBelow = getNumsFromLine(lineBelow) if lineBelow != "" else []
    
    left = max(0,idx-1)
    center = idx
    right = min(len(line)-1,idx+1)
    idxToCheck=[left,center,right]

    ar = []
    for i in idxToCheck:
        for num in numsAbove:
            if i in range(num["start"],num["end"]+1):
                if not isNumInAr(ar, num):
                    ar.append(num)
        for num in nums:
            if i in range(num["start"],num["end"]+1):
                if not isNumInAr(ar, num):
                    ar.append(num)
        for num in numsBelow:
            if i in range(num["start"],num["end"]+1):
                if not isNumInAr(ar, num):
                    ar.append(num)
    if len(ar) == 2:
        prod = ar[0]["value"]*ar[1]["value"]
        return prod
    return 0
        
def getGearSum(lineAbove, line, lineBelow):
    idxAr = getIdxFromStar(line)
    lineSum = 0
    if idxAr == []:
        return 0
    for idx in idxAr:
        lineSum += getAdjUniqueNumSum(idx, line, lineAbove, lineBelow)
    
    return lineSum
            
gearSum = 0
for i, line in enumerate(lines):

    line = line.strip()
    lineAbove = lines[i - 1].strip() if i > 0 else ""
    lineBelow = lines[i + 1].strip() if i < len(lines) - 1 else ""

    addToPartNrAr(lineAbove, line, lineBelow)
    gearSum += getGearSum(lineAbove, line, lineBelow)

print(numAr)

print("Part1:",sum(numAr))
print("Part2:",gearSum)

test = 1
