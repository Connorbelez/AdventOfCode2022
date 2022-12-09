

d = []
file = "/Users/connorbeleznay/Projects/Personal/AdventOfCode/2022/Day1/data1.txt"
with open(file) as f:
    lines = f.readlines()
    totalElfCalories = 0
    minCal = 0
    for line in lines:
        val = line.strip()
        print("VAL: ", val, " Is num: ", val.isnumeric())
        if val.isnumeric():
            totalElfCalories += int(val)
        else:
            d.append(totalElfCalories)
            totalElfCalories = 0
            #finished counting elf calories, check if its top 3 then reset
            d.sort(reverse=True)
            if len(d) > 3:
                d.pop()

    print(d)
                
