
lines = open("data.txt", "r").readlines()

#--- Part 1
maxCal = 0
sum = 0
for l in lines:
    if l == "\n":                   
        maxCal = max(maxCal,sum)
        sum = 0
    else:
        sum += int(l)
print("Part 1:", maxCal)

#--- Part 2
sumAr = []
sum = 0
for l in lines:
    if l == "\n":
        sumAr.append(sum)
        sum = 0
    else:
        sum += int(l)
sumAr.sort(reverse=True)
print("Part 2:", sumAr[0]+sumAr[1]+sumAr[2])




