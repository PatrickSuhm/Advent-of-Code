def getColorCnt(sub):
    r,g,b = 0, 0, 0
    for s in sub:
        for c in ["red","green","blue"]:
            if c in s:
                d = s.replace(c,"")
                if d and c=="red":
                    r+=int(d)
                if d and c=="green":
                    g+=int(d)
                if d and c=="blue":
                    b+=int(d)
    return r,g,b

def part1(lines):
    idSum = 0
    gid = 0
    for l in lines:
        gid+=1
        g = l.strip().split(":")[1].split(";")
        adId = True
        for sub in g:
            r,g,b = getColorCnt(sub.split(","))
            if r>12 or g>13 or b>14:
                adId = False
                break
        if adId:
            idSum += gid
    return idSum

def part2(lines):
    gi = 0
    for l in lines:
        g = l.strip().split(":")[1].split(";")
        rmax = 0
        gmax = 0
        bmax = 0
        for sub in g:
            r,g,b = getColorCnt(sub.split(","))
            rmax = max(rmax, r)
            gmax = max(gmax, g)
            bmax = max(bmax, b)
        p = rmax*gmax*bmax
        gi+=p
    return gi

lines = open("data.txt","r").readlines()
print("Part1:",part1(lines))
print("Part2:",part2(lines))
