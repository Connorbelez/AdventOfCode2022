import numpy as np

f = open("2022/Day8/data1.txt", "r")
# f = open("data.txt", "r")
# treeset = set()
# treeset.add((0,0))
# treeset.add((0,0))
# treeset.add((1,0))
# treeset.add((0,1))
# print(treeset)

# l = [1,2,3,4,5,6,7,8,9]
# for i in range(len(l)-1,-1,-1):
#     print(l[i])

def checkUp(index, matrix):
    pass

def sol2(f):
    lines = f.readlines()
    matrix = [list(line.strip()) for line in lines]
    intMatrix = np.array(matrix, dtype=int)
    
    # mCol = intMatrix[:,0]
    #mRow = intMatrix[0,:]
    # print(mCol)
    largestTreeCount = 0
    for row in range(1,len(matrix)-1):
        
        for col in range(1,len(matrix[0])-1):
            
            tree = intMatrix[row][col]
            treeIndex = (row,col)
            treeCountL = 0
            treeCountR = 0
            treeCountAbove = 0
            treeCountBelow = 0
            #check up
            mCol = intMatrix[:,col]
            mRow = intMatrix[row,:]
            

            treesAbove = np.flip(mCol[:row])
            
            if row < len(mCol) -1:
                treesBelow = mCol[row+1:]
            else:
                treesBelow = []
                
            treesLeft = np.flip(mRow[:col])
            
            if col < len(mRow) -1:
                treesRight = mRow[col+1:]
            else: 
                treesRight = []
            
            for tree in treesAbove:
                treeCountAbove += 1
                if tree >= intMatrix[row][col]:
                    break
                    
            for tree in treesBelow:
                treeCountBelow += 1
                if tree >= intMatrix[row][col]:
                    break

            for tree in treesLeft:
                treeCountL += 1
                if tree >= intMatrix[row][col]:
                    break
            
            for tree in treesRight:
                treeCountR +=1 
                if tree >= intMatrix[row][col]:
                    break
            
            
            treeCount = treeCountAbove * treeCountBelow * treeCountL * treeCountR
            if treeCount > largestTreeCount:
                largestTreeCount = treeCount
    print(largestTreeCount)


def sol1(f):
    lines = f.readlines()
    matrix = [list(line.strip()) for line in lines]
    intMatrix = np.array(matrix, dtype=int)
    treeSet = set()
    #l2R
    lastRow = len(intMatrix) -1
    lastCol = len(intMatrix[0]) -1
    
    for row in range(len(intMatrix)):
        tallestYet = intMatrix[row][0]
        treeSet.add((row,0))
        for col in range(len(intMatrix[0])):
            if intMatrix[row][col] > tallestYet:
                tallestYet = intMatrix[row][col]
                treeSet.add((row,col))
    
    #r2L
    for row in range(len(intMatrix)):
        tallestYet = intMatrix[row][lastCol]
        treeSet.add((row,lastCol))
        
        for col in range(lastCol,-1,-1):
            if intMatrix[row][col] > tallestYet:
                tallestYet = intMatrix[row][col]
                treeSet.add((row,col))

    #t2B
    for col in range(len(intMatrix[0])):
        tallestYet = intMatrix[0][col]
        treeSet.add((0,col))
        for row in range(len(intMatrix)):
            if intMatrix[row][col] > tallestYet:
                tallestYet = intMatrix[row][col]
                treeSet.add((row,col))
    
    #b2T
    for col in range(len(intMatrix[0])):
        tallestYet = intMatrix[lastRow][col]
        treeSet.add((lastRow,col))
        
        for row in range(lastRow,-1,-1):
            if intMatrix[row][col] > tallestYet:
                tallestYet = intMatrix[row][col]
                treeSet.add((row,col))

    print(len(treeSet))
    
# sol1(f)
sol2(f)