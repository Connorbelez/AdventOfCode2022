d = []
file = "/Users/connorbeleznay/Projects/Personal/AdventOfCode/2022/Day1/data1.txt"
with open(file) as f:
    lines = f.readlines()
    calories = 0
    elf = 0
    min = 0
    for line in lines:
        val = line.strip()
        print("VAL: ", val, " Is num: ", val.isnumeric())
        if val.isnumeric():
            calories += int(val)
        else:
            if len(d) == 0:
                d.append(calories)
                min = calories
                calories = 0
            elif len(d) < 3:
                for i,v in enumerate(d):
                    if calories > v:
                        d.insert(i,calories)
                        calories = 0
                        min = d[len(d)-1]
                        break
            elif calories > min:
                for i,v in enumerate(d):
                    if calories > v:
                        d.insert(i,calories)
                        break
                calories = 0
                d.pop()
                min = d[len(d)-1]
    print(d)
                
