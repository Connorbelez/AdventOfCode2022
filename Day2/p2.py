# The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

# The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

# In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
# In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
# In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
# Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.


#  X means you need to lose, 
#  Y means you need to end the round in a draw,
#  and Z means you need to win. Good luck!"


def calculateScore(line, cDict,RPS):
    line = line.strip()
    mv = line.split(" ")
    p1 = cDict[mv[0]]
    wl = mv[1]

    if wl == "X":
        #lose
        print("LOSE, ", "Opponent: ", RPS[p1], " You: ", RPS[(p1+2)%3], "Total: ",(p1+2)%3 + 1)
        return (p1+2)%3 + 1
    elif wl == "Y":
        #tie
        print("tie, ", "Opponent: ", RPS[p1], " You: ", RPS[p1], "Total: ", p1 + 4)
        return p1 + 4
    else:
        print("win, ", "Opponent: ", RPS[p1], " You: ", RPS[(p1+1)%3], "Total: ",(p1+1)%3 + 7)
        return (p1+1)%3 + 7
    
    
    

def main():
    # moveDict = {"R":0,"P":1,"S":2}
    RPS = ["R","P","S"]
    cDict = {"A":0, "B":1, "C":2}
    
    #Test Cases
    print(calculateScore("A Z", cDict, RPS), "Should be 3")
    print(calculateScore("A Y", cDict, RPS),"should be 4")
    print(calculateScore("A X", cDict, RPS), )
    print(calculateScore("B Z", cDict, RPS))
    print(calculateScore("B Y", cDict, RPS))
    print(calculateScore("B X", cDict, RPS))
    print(calculateScore("C Z", cDict, RPS))
    print(calculateScore("C Y", cDict, RPS))
    print(calculateScore("C X", cDict, RPS))
    
    
    file = open("data2.txt")
    with open("data2.txt") as f:
        total = 0
        for line in file:
            total += calculateScore(line, cDict,RPS)
    print(total)

if __name__ == "__main__":
    main()