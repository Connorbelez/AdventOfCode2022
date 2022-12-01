def getCalories(file):
    elf = 0
    with open(file) as f:
        lines = f.readlines()
        calories = 0
        for line in lines:

            val = line.strip()
            print("VAL: ", val, " Is num: ", val.isnumeric())
            if val.isnumeric():
                calories += int(val)
            else:
                if elf < calories:
                    elf = calories
                calories = 0
                
        return elf

if __name__ == "__main__":
    print(getCalories("/Users/connorbeleznay/Projects/Personal/AdventOfCode/2022/Day1/data1.txt"))