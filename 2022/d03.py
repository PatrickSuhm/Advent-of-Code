
lines = open("data.txt", "r").readlines()
charList = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getPrioOfChar(char):
    for i,c in enumerate(charList):
        if char == c:
            return i

#--- Part 1
cnt = 0
for l in lines:
    length = len(l)-1
    left = l[0:int(length/2)]
    right = l[int(length/2):-1]
    char = "-1"
    for le in left:
        if le in right:
            char = le
    cnt += getPrioOfChar(char)
print("Part 1:", cnt)

#--- Part 2
cnt = 0
line12 = []
for i,l in enumerate(lines):
    if (i+1)%3 == 0:
        for char in charList:
            if char in l and char in line12[0] and char in line12[1]:
                break
        cnt += getPrioOfChar(char)
        line12 = []
    else:
        line12.append(l)
print("Part 2:",cnt)



