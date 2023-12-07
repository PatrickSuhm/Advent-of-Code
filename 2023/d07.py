import math
f = open("data.txt","r")
lines = f.readlines()

for part in  [1,2]:
    if part == 1:
        strength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    else:
        strength = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    data = []
    for line in lines:
        data.append(line.strip().split())

    def getStrengthOfIndivid(card):
        ind = 0
        for i,c in enumerate(card):
            cPos = (5-i)
            for j,s in enumerate(strength):
                stren = math.log((len(strength)-j))
                if c == s:
                    ind += stren*100**cPos
        return ind
            
    def getStrengthOfCard(card):
        charCount = {}
        for char in card:
            charCount[char] = charCount.get(char, 0) + 1

        if part == 1:
            jCnt = -1
            j = False
        else:
            jCnt = 0
            j = True if "J" in card else False
            if j:
                jCnt = charCount["J"]

        if any(count == 5 for count in charCount.values()): 
            return 7
        
        if any(count == 4 for count in charCount.values()):
            if j:
                return 7
            return 6

        if (len(charCount.values()) == 2 and 2 in charCount.values() and 
            3 in charCount.values()): 
            if j:
                return 7
            return 5
        
        if any(count == 3 for count in charCount.values()): 
            if j:
                return 6
            return 4

        pcnt = 0
        for count in charCount.values():
            if count == 2:
                pcnt += 1

        if pcnt == 2:
            if jCnt == 1:
                return 5
            if jCnt == 2:
                return 6
            return 3
        
        if pcnt == 1: 
            if jCnt == 1 or jCnt == 2:
                return 4
            return 2

        if all(count == 1 for count in charCount.values()):
            if j:
                return 2
            return 1

        return 0

    def assignNumToDataVal(dataVal):
        card = dataVal[0]
        return getStrengthOfCard(card)

    def assignIndivid(dataVal):
        card = dataVal[0]
        return getStrengthOfIndivid(card)

    sortedObjects = sorted(data, key=assignNumToDataVal)

    for i,s in enumerate(sortedObjects):
        sortedObjects[i].append(assignNumToDataVal(s))
        sortedObjects[i].append(assignIndivid(s))

    dict = {}
    for subarray in sortedObjects:
        key = subarray[2]
        dict.setdefault(key, []).append(subarray)
    grouped = list(dict.values())

    final = []
    for i,group in enumerate(grouped):
        if len(group) > 1:
            grouped[i] = sorted(group,key=assignIndivid)
            for g in grouped[i]:
                final.append(g)
        else:
            final.append(group[0])
        test = 1

    total = 0
    for i,da in enumerate(final):
        pro = (i+1)*int(da[1])
        total += pro
    
    print("Part"+str(part)+":",total)
