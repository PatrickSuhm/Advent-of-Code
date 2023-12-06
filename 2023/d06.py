f = open("data.txt","r")
lines = f.readlines()

for part in [1,2]:
    if part == 1:
        times = [int(i) for i in lines[0].split(":")[1].strip().split()]
        records = [int(i) for i in lines[1].split(":")[1].strip().split()]
    else:
        times = [int(lines[0].split(":")[1].strip().replace(" ",""))]
        records = [int(lines[1].split(":")[1].strip().replace(" ",""))]

    prod = 1
    for ti,rec in zip(times,records):
        winCnt = 0
        for i,t in enumerate(range(ti)):
            t = t+1 
            v = t 
            dist = (ti-t)*v
            if dist > rec:
                winCnt += 1
        prod *= winCnt

    print("Part"+str(part)+":",prod)