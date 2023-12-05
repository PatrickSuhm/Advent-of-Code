f = open("data.txt","r")
lines = f.readlines()

for part in [1,2]:
    seeds = [int(i) for i in lines[0].strip().split(": ")[1].split(" ")]

    name = ""
    dataAr = []
    data = {}
    for line in lines[1:]:
        line = line.strip()
        if not line or line == "\n":
            continue
        
        if "map:" in line:
            name = line.replace(" map:", "")
            dataAr = []
        else:
            dataAr.append([int(i) for i in line.split()])
        if dataAr != []:
            data[name] = dataAr

    if part == 2:
        seedList = []
        rs = []
        while seeds: 
            start = seeds.pop(0)
            cnt = seeds.pop(0)
            end = start+cnt 
            rs.append([start, end])
        seeds = seedList
        for r in rs:
            for s in range(r[0],r[1]):
                seedList.append(s)

    def mapSeed(seed, ar):
            destiStart = ar[0]
            srcStart = ar[1]
            dist = ar[2]
            srcEnd = ar[1]+dist
            if seed in range(srcStart, srcEnd):
                mappedSeed = destiStart + seed-srcStart
                return mappedSeed
            else:
                return -1

    minLoc = 1e33
    for oriSeed in seeds:
        mapped = oriSeed
        for map in data:
            candi = 1e33
            for ar in data[map]: 
                ma = mapSeed(mapped, ar)
                if ma != -1: 
                    if ma < candi:
                        candi = ma
            if candi == 1e33:
                candi = mapped
            mapped = candi
                    
        minLoc = min(minLoc, mapped)
    
    print("Part"+str(part)+":",minLoc)
