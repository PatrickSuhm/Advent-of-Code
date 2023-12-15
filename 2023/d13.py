f = open("data.txt","r")
pattern = [lines.split("\n") for lines in f.read().split("\n\n")]

def transpose(lines):
    trans = []
    for i in range(len(lines[0])):
        col = ""
        for j in range(len(lines)):
            col+=lines[j][i]
        trans.append(col)
    return trans

def difference(line1, line2):
    if len(line1) != len(line2):
        return 1e99
    differences = 0
    for char1, char2 in zip(line1, line2):
        if char1 != char2:
            differences += 1
    return differences

def goOutIsOk(i, lines, allowedErr):
    numErrLines = 0
    for p, p2 in zip(range(i,len(lines)), range(i-1, -1,-1)):
        if allowedErr == 0:
            if difference(lines[p], lines[p2]) > 0:
                numErrLines += 1
        else:
            if difference(lines[p], lines[p2]) > allowedErr:
                numErrLines = 1e99
            if difference(lines[p], lines[p2]) == allowedErr:
                numErrLines += 1
    return True if numErrLines==allowedErr else False

def findRowMirrorIdx(pat, allowedErr):
    prev = ""
    for i, line in enumerate(pat):
        if difference(line, prev) <= allowedErr:
            if goOutIsOk(i, pat, allowedErr):
                return i
        prev = line
    return -1

def findReflIdx(pat,allowedErr):
    idx = findRowMirrorIdx(pat,allowedErr)
    if idx == -1:
        return findRowMirrorIdx(transpose(pat),allowedErr)
    else:
        return 100*(idx)

for part in [1,2]:
    ans = 0
    for i,pat in enumerate(pattern):
        ae1 = findReflIdx(pat,1 if part == 2 else 0)
        if -1==ae1:
            ans += findReflIdx(pat,0)
        else:
            ans += ae1
    print("Part"+str(part)+":",ans)
