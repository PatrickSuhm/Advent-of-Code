
lin = open("data.txt", "r").readlines()[0]

def processedChars(lenOfUnique):
    for i in range(len(lin)):                           # go over inputstr
        if i >= lenOfUnique-1:
            checkList = []
            for j in range(lenOfUnique):
                checkList.append(lin[i-j])
            if len(set(checkList)) == lenOfUnique:      # set() reduces douplicates
                return i+1
                    
#--- Part 1
print("Part 1", processedChars(4))

#--- Part 2
print("Part 2", processedChars(14))



