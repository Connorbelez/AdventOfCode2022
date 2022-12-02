


def calculateScore(line, mDict, cDict,RPS):
    line = line.strip()
    mv = line.split(" ")
    p1 = mDict[cDict[mv[0]]]
    p2 = mDict[cDict[mv[1]]]

    if RPS[(p1+1)%3] == RPS[p2]:
        print("Line: ", line, " P1: ", RPS[p1], " P2: ", RPS[p2], " P2 wins with: ", 7+p2)
        return 7 + p2
    elif RPS[(p1+2)%3] == RPS[p2]:
        print("Line: ", line, " P1: ", RPS[p1], " P2: ", RPS[p2], " P1 wins with: ", 1 + p2)
        return 1 + p2
    else:
        print("Draw")
        return 4 + p2

#Generate test cases for this program:

def main():
    moveDict = {"R":0,"P":1,"S":2}
    RPS = ["R","P","S"]
    cDict = {"X":"R","Y":"P","Z":"S", "A":"R", "B":"P", "C":"S"}
    print(calculateScore("A Z", moveDict, cDict, RPS), "Should be 3")
    print(calculateScore("A Y", moveDict, cDict, RPS),"should be 5")
    print(calculateScore("A X", moveDict, cDict, RPS))
    print(calculateScore("B Z", moveDict, cDict, RPS))
    print(calculateScore("B Y", moveDict, cDict, RPS))
    print(calculateScore("B X", moveDict, cDict, RPS))
    print(calculateScore("C Z", moveDict, cDict, RPS))
    print(calculateScore("C Y", moveDict, cDict, RPS))
    print(calculateScore("C X", moveDict, cDict, RPS))
    
    
    file = open("data2.txt")
    with open("data2.txt") as f:
        total = 0
        for line in file:
            total += calculateScore(line, moveDict, cDict,RPS)
    print(total)

if __name__ == "__main__":
    main()