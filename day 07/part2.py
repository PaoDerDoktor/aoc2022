def get_dir_size(dirTree: dict[str, set[str]], directDirSize: dict[str, int], finalSizes: dict[str, int], dir: str) -> int:
    travelStack: list[str] = [dir]
    visited:     set[str]  = set()
    
    while len(travelStack) != 0:
        currentDir: str = travelStack[-1]
        
        expand: bool = False
        
        childrens: set[str] = dirTree[currentDir]
        
        for child in childrens:
            if child not in visited:
                travelStack.append(child)
                expand = True
        
        if not expand:
            finalSizes[currentDir] = directDirSize[currentDir] + sum([finalSizes[child] for child in childrens])
            travelStack.pop()
            visited.add(currentDir)

    return finalSizes[dir]

def day7_part2_main() -> int:
    with open("day 07/inputs.txt", 'r') as inFile:
        dirTree:       dict[str, set[str]] = {}
        directDirSize: dict[str, int]      = {}
        
        pwd: str = '/' # currentPath
        pc:  int = 0   # Current line
        
        lines: list[list[str]] = [l.strip().split() for l in inFile.readlines()]
        
        while pc != len(lines):
            line: list[str] = lines[pc]
            if line[0] == '$': # Line is a command
                if line[1] == "cd": # Command is a directory change
                    if line[2] == "/": # Program should go to root
                        pwd = "/"
                    elif line[2] == "..": # Program should go back
                        lastBranch: int = -(pwd[::-1][1:].index('/')+1)
                        pwd = pwd[:lastBranch]
                    else: # Program should enter a new folder
                        pwd += line[2] + "/"
                    
                    pc += 1
                elif line[1] == "ls": # Command is a listing of content
                    pc += 1
                    
                    if pwd not in dirTree:
                        dirTree[pwd] = set()
                    
                    if pwd not in directDirSize:
                        directDirSize[pwd] = 0
                    
                    while pc != len(lines) and lines[pc][0] != '$': # While not at EOF or next command...
                        if lines[pc][0] == "dir": # Item is a folder
                            dirTree[pwd].add(pwd+lines[pc][1]+"/")
                        else: # Item is a file
                            directDirSize[pwd] += int(lines[pc][0])
                        pc += 1
        
        # Recursively compute folder sizes from direct sizes and dirTree
        finalSizes: dict[str, int] = {k: -1 for k in directDirSize}
        
        rootSize: int = get_dir_size(dirTree, directDirSize, finalSizes, '/')
        
        totalSpace: int = 70000000
        unusedSpace: int = totalSpace - rootSize
        updateSpace: int = 30000000
        requiredSpace: int = updateSpace - unusedSpace
        
        bigEnoughSizes: list[int] = sorted([size for size in finalSizes.values() if size >= requiredSpace])
        print(bigEnoughSizes)
        
        return bigEnoughSizes[0]

if __name__ == "__main__":
    print(day7_part2_main())
