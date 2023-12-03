lines = open("data.txt", "r").read()
pairs = lines.split("\n\n")
pairs = [(eval(p.split("\n")[0]), eval(p.split("\n")[1]) )for p in pairs]

def isRightOrder(le,ri):
    if type(le) is int and type(ri) is int:
        if le < ri:
            return True
        elif le == ri:
            return None
        else:
            return False
    
    elif type(le) is int and type(ri) is list:
        le = [le]
    
    elif type(le) is list and type(ri) is int:
        ri = [ri]

    for l,r in zip(le,ri):     
        out = isRightOrder(l, r)
        if out == False or out == True:
            return out
    if len(le) > len(ri):
        return False
    elif len(le) < len(ri):
        return True
    else:
        return None

sum = 0
for i,p in enumerate(pairs):  
    #print(p,end = " ")
    if isRightOrder(p[0],p[1]):
        #print("true")
        sum += i+1
    #else: print("false")
print("Part 1:", sum)

pairs.append(([[2]],[[6]]))
packets = []
for p in pairs:
    packets.append(p[0])
    packets.append(p[1])


for i in range(len(packets), 1, -1): 
    for j in range(0, i-1):
        temp = packets[j+1]
        if not isRightOrder(packets[j], packets[j+1]):
            packets[j+1] = packets[j]
            packets[j] = temp

prod = 1
for i,p in enumerate(packets):
    if p == [[2]] or p == [[6]]:
        prod *= i+1

print("Part 2:", prod)
    