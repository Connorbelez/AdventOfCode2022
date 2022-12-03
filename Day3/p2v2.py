
def fb(group):

    if len(group) !=3:
        print("Error")
        exit()
    for i in range(3):
        group[i] = group[i].strip()
    print(group)
    return (set(group[0]) & set(group[1]) & set(group[2])).pop()
    
    
with open("data3.txt") as f:
    data = f.readlines()
    prev = 0
    groups = [data[i:i + 3] for i in range(0, len(data), 3)]
    pt = 0
    
    for group in groups:
        priority = ord(fb(group))
        if priority >= 97:
            priority -= 96
        else:
            priority -= 38
        pt += priority
    print(pt)
        