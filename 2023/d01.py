f = open("data.txt","r")

def lineToDig(l):
    numberMapping = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }
    for word, number in numberMapping.items():
        l = l.replace(word, number)
    return l

dat1 = []
dat2 = []
codes1 = []
codes2 = []

for l in f:
    dat2.append(lineToDig(l.strip()))
    dat1.append(l.strip())

for l in dat1:
    num = ""
    for c in l:
        if c.isdigit():
            num += c
    codes1.append(int(num[0]+num[-1]))
    
for l in dat2:
    num = ""
    for c in l:
        if c.isdigit():
            num += c
    codes2.append(int(num[0]+num[-1]))

print("Part1:",sum(codes1))
print("Part2:",sum(codes2))
