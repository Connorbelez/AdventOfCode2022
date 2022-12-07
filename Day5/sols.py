
f = open("data5.txt", "r")

def sol1(file):
    data = file.readlines()
    cols = data[8]
    instructions = data[10:]
    stacks = []
    startingMatrix = data[:8]
    values = [i for i in range(1,10)]
    
    for value in values:
        deque = []
        col = cols.index(str(value))
        for row in startingMatrix:
            if row[col] != " ":
                deque.insert(0, row[col])
        stacks.append(deque)
    
    for line in instructions:
        print(line)
        lp = line.strip().split(" ")
        print(lp)
        num = int(lp[1])
        s = int(lp[3])
        d = int(lp[5])
        
        # print()
        for i in range(num):
            stacks[d-1].append(stacks[s-1].pop())
        # stacks[d-1] = stacks[d-1]+(stacks[s-1][-num:])
        # stacks[s-1] = stacks[s-1][:-num]
        
    for stack in stacks:
        print(stack.pop())
    
    


def sol2(file):
    data = file.readlines()
    cols = data[8]
    instructions = data[10:]
    stacks = []
    startingMatrix = data[:8]
    values = [i for i in range(1,10)]
    
    for value in values:
        deque = []
        col = cols.index(str(value))
        for row in startingMatrix:
            if row[col] != " ":
                deque.insert(0, row[col])
        stacks.append(deque)
    
    for line in instructions:
        print(line)
        lp = line.strip().split(" ")
        print(lp)
        num = int(lp[1])
        s = int(lp[3])
        d = int(lp[5])
        
        stacks[d-1] = stacks[d-1]+(stacks[s-1][-num:])
        stacks[s-1] = stacks[s-1][:-num]
        
    for stack in stacks:
        print(stack.pop())
    
    
    
    
sol1(f)
sol2(f)
  