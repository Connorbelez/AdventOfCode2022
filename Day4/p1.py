# Parse the input data into a list of tuples, each containing the start and end of the range
# e.g. [(2, 4), (6, 8), ...]

f = open("data4.txt", "r")

def parse(input_data):
    total = 0
    lines = []
    for line in input_data:
        l = line.strip().split(",")
        rp = l[0].split("-") + l[1].split("-")
        rp = [int(x) for x in rp]

        lines.append(rp)
    
    
    for i,line in enumerate(lines):
        print(line)
        if line[0] >= line[2] and line[1] <= line[3]:
            total +=1
        elif line[0] <= line[2] and line[1] >= line[3]:
            total +=1
    return total

    
        
print(parse(f))