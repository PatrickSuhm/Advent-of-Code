f = open("data.txt","r")
lines = f.readlines()

pointsPart1 = 0
def part1(pointsPart1):
    mult = 0
    for m in mine:
        if m in winning:
            if mult == 0: mult = 1
            else: mult*=2
    pointsPart1 += mult
    return pointsPart1

def getNumWinning():
    cnt = 0
    for m in mine:
        if m in winning:
            cnt+=1
    return cnt


winningCntAr = []

for l in lines:
    l = l.split(":")[1].split("|")
    winningc =  l[0].strip().split(" ")
    minec = l[1].strip().split(" ")

    winning = []
    for w in winningc:
        if w != "":
            winning.append(int(w))
    mine = []
    for m in minec:
        if m!="":
            mine.append(int(m))
    
    pointsPart1 = part1(pointsPart1)

    winningCntAr.append(getNumWinning())

cardCntsAr = [0]*len(lines)

def rec(start, end):
    for cardIdx in range(start,end):
        cardWinCnt = winningCntAr[cardIdx]
        cardCntsAr[cardIdx] += 1
        if cardWinCnt != 0:
            rec(cardIdx+1,cardIdx+cardWinCnt+1)


rec(0,len(lines))
        
print("Part1:",pointsPart1)
print("Part2:",sum(cardCntsAr))

