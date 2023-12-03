
def readNewCmd(lines):
    if len(lines) > 0:
        l = lines.pop(0)
        if "addx" in l:
            cmd = "addx"
            val = int(l.split(" ")[1])
        else:
            cmd = "noop"
            val = 0
    else:
        cmd = "stop"
        val = 0
    return cmd, val

def printChar(cyc, c):
    if cyc == 39:
        print(c)
    else:
        print(c, end="")

cycDic = {"":0, "addx": 2, "noop": 1}

#--- Part 1
lines = open("data.txt", "r").readlines()
sum = 0
x = 1
iCnts = [20, 60, 100, 140, 180, 220]
cmd = ""
val = 0
cntDel = 0
for cnt in range(1,iCnts[-1]+1):
    if cntDel == cycDic[cmd]:    
        cmd, val = readNewCmd(lines)
        cntDel = 0
    cntDel += 1
    if cnt in iCnts:
        sum += x*cnt
    if cmd == "addx" and cntDel == 2:
        x += val
print("Part 1:", sum)

#--- Part 2
lines = open("data.txt", "r").readlines()
print("Part 2:")
x = 1               
cmd = ""
val = 0
cntDel = 0
cyc = 0
while True:
    if cntDel == cycDic[cmd]:    
        cmd, val = readNewCmd(lines)
        if cmd == "stop": break
        cntDel = 0
    cntDel += 1
    cyc = cyc%40
    if x-1 == cyc or x == cyc or x+1 == cyc:
        printChar(cyc, "#")
    else:
        printChar(cyc, ".")
    if cmd == "addx" and cntDel == 2:
        x += val
    cyc += 1