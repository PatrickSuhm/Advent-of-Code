
class Knot:
    def __init__(s, start = 0):         
        s.x = start
        s.y = start
        
    def mv(s, dirStr):                   
        if dirStr == "U":
            s.y += 1
        elif dirStr == "D":
            s.y -= 1
        elif dirStr == "R":
            s.x += 1
        elif dirStr == "L":
            s.x -= 1
    
    def getXY(s):
        return [s.x, s.y]

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

def simulate(lines, numKnots):
    knots = [Knot() for i in range(numKnots)]
    visited = set()
    visited.add(tuple([0,0]))   
    for l in lines:
        dirStr = l.split(" ")[0]
        distance = int(l.split(" ")[1])
        for step in range(distance):
            knots[0].mv(dirStr)                       
            for ind in range(1,numKnots):
                delx = knots[ind-1].x - knots[ind].x
                dely = knots[ind-1].y - knots[ind].y
                knots[ind].x += delx - sign(delx)
                knots[ind].y += dely - sign(dely)
                if not (abs(delx) > 1 and abs(dely) > 1):
                    if abs(delx) > 1 and abs(dely) > 0:
                        knots[ind].y = knots[ind-1].y
                    if abs(dely) > 1 and abs(delx) > 0:
                        knots[ind].x = knots[ind-1].x
                if abs(delx) > 1 or abs(dely) > 1:
                    if ind == numKnots - 1:
                        visited.add(tuple(knots[ind].getXY()))
    return len(visited)

lines = open("data.txt", "r").readlines()

#--- Part 1
ans = simulate(lines, 2)
print("Part 1:", ans)

#--- Part 2
ans = simulate(lines, 10)        
print("Part 2:", ans)
