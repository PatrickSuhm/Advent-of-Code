lines = open("data.txt","r").readlines()
lines = [line.split("@") for line in lines]
data = [ [[int(li) for li in line[0].split(",")], [int(li) for li in line[1].split(",")]] for line in lines]

least = 200000000000000
most = 400000000000000
colliCnt = 0
for i in range(len(data)):
    vx1 = data[i][1][0]
    vy1 = data[i][1][1]
    px1 = data[i][0][0]
    py1 = data[i][0][1]
    for j in range(i+1,len(data)):
        vx2 = data[j][1][0]
        vy2 = data[j][1][1]
        px2 = data[j][0][0]
        py2 = data[j][0][1]
        if (vx1*vy2 - vx2*vy1) != 0:
            solx = (-px1*vx2*vy1 + px2*vx1*vy2 + py1*vx1*vx2 - py2*vx1*vx2)/(vx1*vy2 - vx2*vy1)
            if solx <= most and solx >= least:
                t1 = (solx-px1)/vx1
                t2 = (solx-px2)/vx2
                soly = vy1*t1 + py1
                if t1 > 0 and t2 > 0:
                    if soly <= most and soly >= least:
                        colliCnt += 1
print("Part1:",colliCnt)

import sympy as sym
px, py, pz, vx, vy, vz = sym.symbols("px, py, pz, vx, vy, vz", integer=True)
numHs = 3
sl = []
for i in range(1, numHs + 1):
    sl.append(sym.symbols(f't{i}', integer=True))
eq = []
for i in range(numHs):
    vxi = data[i][1][0]
    vyi = data[i][1][1]
    vzi = data[i][1][2]
    pxi = data[i][0][0]
    pyi = data[i][0][1]
    pzi = data[i][0][2]
    eq.append( vxi*sl[i] + pxi - (vx*sl[i] + px) )
    eq.append( vyi*sl[i] + pyi - (vy*sl[i] + py) )
    eq.append( vzi*sl[i] + pzi - (vz*sl[i] + pz) )
sol = sym.solve(eq,domain = sym.S.Integers)[0]
print("Part2:",sol[px]+sol[py]+sol[pz])
