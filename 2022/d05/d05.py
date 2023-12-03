
lines = open("data.txt", "r").readlines()
stackOri = ["GJWRFTZ","MWG", "GHNJ","WNCRJ","MVQGBSFW","CWVDTRS","VGZDCNBH","CGMNJS","LDJCWNPG"]

#--- Part 1
stack = stackOri.copy()
for l in lines[10:]:
    data = l.split()
    num = int(data[1])
    start = int(data[3])-1
    end = int(data[5])-1
    for i,c in enumerate(stack[start]):
        stack[end] = c + stack[end]
        if i==num-1:
            break
    stack[start] = stack[start][num:]
out = ""
for s in stack:
    out+=s[0]
print("Part 1:",out)

#--- Part 2
stack = stackOri.copy()
for l in lines[10:]:
    data = l.split()
    num = int(data[1])
    start = int(data[3])-1
    end = int(data[5])-1
    stack[end] = stack[start][0:num]+stack[end]
    stack[start] = stack[start][num:]
out = ""
for s in stack:
    out+=s[0]
print("Part 2:", out)



