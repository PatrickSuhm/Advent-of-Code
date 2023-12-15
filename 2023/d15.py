f = open("data.txt","r")
vals = f.readline().strip().split(",")

def hashFun(val):
    h = 0
    for c in val:
        h += ord(c)
        h = (h * 17)%256
    return h

class lense:
    def __init__(s, label, focLen):
        s.label = label
        s.focLen = focLen
sumH = 0
boxes = [[] for _ in range(256)]
for val in vals:
    sumH += hashFun(val)
    
    if "-" in val:
        label = val.split("-")[0]
        boxNum = hashFun(label)
        for i, l in enumerate(boxes[boxNum]):
            if l.label == label:
                boxes[boxNum].pop(i) 
                test = 1

    if "=" in val:
        label = val.split("=")[0]
        boxNum = hashFun(label)
        lNew = lense(label,val.split("=")[1])
        if len(boxes[boxNum]) == 0:
            boxes[boxNum].append(lNew)
        else:
            labelExists = False
            for i,lOld in enumerate(boxes[boxNum]):
                if lNew.label == lOld.label:
                    labelExists = True
                    boxes[boxNum][i] = lNew
            if not labelExists:
                boxes[boxNum].append(lNew)

res = 0
for i,box in enumerate(boxes):
    for j,l in enumerate(box):
        res += (1+i)*(1+j)*int(l.focLen)

print("Part1:",sumH)
print("Part2:",res)