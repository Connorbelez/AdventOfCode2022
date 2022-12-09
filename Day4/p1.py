# Parse the input data into a list of tuples, each containing the start and end of the range
# e.g. [(2, 4), (6, 8), ...]

f = open("data4.txt", "r")

def parse(input_data):
    total = 0
    lines = []

    lines = [ [ int(x) for x in (line.strip().split(",")[0].split("-") + line.strip().split(",")[1].split("-")) ] for line in input_data ]
    
    for line in lines:
        if line[0] >= line[2] and line[1] <= line[3]:
            total +=1
        elif line[0] <= line[2] and line[1] >= line[3]:
            total +=1
    return total

    
        
print(parse(f))