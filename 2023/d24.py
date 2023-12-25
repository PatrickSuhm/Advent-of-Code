# import sympy as sym
# x, y1, y2, vy1, vy2, vx1, vx2, px1, px2, py1, py2 = sym.symbols("x, y1, y2, vy1, vy2, vx1, vx2, px1, px2, py1, py2")
# y1 = vy1/vx1*(x-px1) + py1
# y2 = vy2/vx2*(x-px2) + py2
# solx = sym.solve(y1-y2, "x")

lines = open("dataFull.txt","r").readlines()
lines = [line.split("@") for line in lines]
data = [ [[int(li) for li in line[0].split(",")], [int(li) for li in line[1].split(",")]] for line in lines]

least = 200000000000000
most = 400000000000000

colliCnt = 0
k = 0
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

        k += 1
        if (vx1*vy2 - vx2*vy1) != 0:
            solx = (-px1*vx2*vy1 + px2*vx1*vy2 + py1*vx1*vx2 - py2*vx1*vx2)/(vx1*vy2 - vx2*vy1)
            if solx <= most and solx >= least:
                t1 = (solx-px1)/vx1
                t2 = (solx-px2)/vx2
                soly = vy1*t1 + py1
                if t1 > 0 and t2 > 0:
                    if soly <= most and soly >= least:
                        print(k, solx, soly)
                        colliCnt += 1

print("Part1:",colliCnt)

