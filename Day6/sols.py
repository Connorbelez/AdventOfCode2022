def sol1(file):
    string = file.readline()
    index = 0
    while index != len(string)-15:
        window = list(string[index:index+14])
        print(window)
        
        if len(window) == len(set(window)):
            break
        index += 1
        
        
        
    return index + 14
        
        
def main():
    with open("data.txt") as file:
        print(sol1(file))
        
if __name__ == "__main__":
    main()