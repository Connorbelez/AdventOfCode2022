
counter = 0
class Directory:
    def __init__(self, name, type, parent=None, size=0):
        self.name = name
        self.children = {}
        self.parent = parent
        self.size = size
    def update_size(self, size):
        self.size += size
        if self.parent:
            self.parent.update_size(size)
    def add_child(self, child):
        self.children[child.name] = child
    def change_dir(self, dir):
        return self.children[dir]
    def __str__(self):
        return "Name: " + self.name + " Size: " + str(self.size)
    
def sol1(file):
    with open(file, "r") as f:
        fline = f.readline()
        Dir = Directory("/","dir")
        root = Dir
        lsFlag = False
        for line in f:
            if l[0] == '$':
                #new command
                lsFlag = False
                if len(l) == 2:
                    #ls
                    #iterate until next command
                    lsFlag = True
                else:
                    #cd:
                    if l[2] == '..':
                        #go up
                        Dir = Dir.parent
                    else:
                        Dir = Dir.change_dir(l[2])
            else:
                #if ls flag is true, add each line to the directory
                if lsFlag:
                    if l[0] == 'dir':
                        newDir = Directory(l[1], l[0], Dir)
                        Dir.add_child(newDir)
                    else:
                        Dir.update_size(int(l[0]))
    sizeReq = 30000000
    DiscAvail = 70000000 - root.size
    val = sizeReq - DiscAvail
    return bfs(root), bfs2(root,val)
        
def bfs(root):
    q = [root]
    counter = 0
    while q:
        node = q.pop(0)
        if node.size <= 100000:
            counter += node.size
        for childName,child in node.children.items():
            q.append(child)
    return counter

def bfs2(root,sizeReq):
    q = [root]
    counter = 0
    canidate = [root]
    min1 = root.size
    while q:
        node = q.pop(0)
        if node.size >= sizeReq and node.size < min1:
            canidate.append(node)
            min1 = node.size
        for childName,child in node.children.items():
            q.append(child)
    for i in canidate:
        print(i)
    return min1

def main():
    file = "/Users/connorbeleznay/Projects/Personal/AdventOfCode/2022/Day7/data.txt"
    num, num2 = sol1(file)
    print(num)
    print(num2)
    
if __name__ == "__main__":
    main()