# Parse the input data into a list of tuples, each containing the start and end of the range
# e.g. [(2, 4), (6, 8), ...]
import re
f = open("data4.txt", "r")

def parse(input_data):
    total = 0
    lines2 = [[int(x) for x in (re.findall("\d+", line))] for line in input_data]
    print(lines2)

    for a1,a2,b1,b2 in lines2:
        if a1 >= b1 and a2 <= b2:
            total +=1

    
        
print(parse(f))