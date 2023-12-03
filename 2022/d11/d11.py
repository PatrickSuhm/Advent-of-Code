lines = open("data.txt", "r").readlines()

class Monkey:
    def __init__(s):
        s.items = []
        s.operation = ""
        s.divisor = -1
        s.true = -1
        s.false = -1
        s.inspections = 0
        
for part in [1, 2]:
    monkeys = []
    for l in lines:
        if "Monkey" in l:
            monkeyNum = int(l.split(" ")[1][:-2])
            monkeys.append(Monkey())
        if "Starting items:" in l:
            monkeys[-1].items = [int(itm) for itm in l[17:-1].split(", ")]
        if "Operation:" in l:
            monkeys[-1].operation = l[13:-1]
        if "Test:" in l:
            monkeys[-1].divisor = int(l[20:])
        if "If true:" in l:
            monkeys[-1].true = int(l[28:])
        if "If false:" in l:
            monkeys[-1].false = int(l[29:])
    new = []
    if part == 2:
        totalDivisor = 1
        for mk in monkeys:
            totalDivisor *= mk.divisor
    for _ in range(20 if part == 1 else 10000):
        for monkey in monkeys:
            for itm in monkey.items:
                monkey.inspections += 1
                old = itm
                exec(monkey.operation)
                if part == 1: new = int(new/3)
                else: new = new%totalDivisor
                if new%monkey.divisor == 0:
                    monkeys[monkey.true].items.append(new)
                else:
                    monkeys[monkey.false].items.append(new)
            monkey.items = []  
    inspList = []
    for mk in monkeys:
        inspList.append(mk.inspections)
    inspList.sort()
    ans = inspList[-2]*inspList[-1]
    print("Part",str(part)+":", ans)

