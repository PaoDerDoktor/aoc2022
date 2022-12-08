def day8_part1_main() -> int:
    with open("day 08/inputs.txt", 'r') as inFile:
        forest: list[list[int]] = [[int(tree) for tree in line.strip()] for line in inFile.readlines()] # Adressed (height, width)
        
        height: int = len(forest)
        width:  int = len(forest[0])
        
        visibleMask: list[list[bool]] = [[False for x in range(width)] for y in range(height)]
        
        # Testing lines
        for y in range(height):
            highest:        int = -1
            reverseHighest: int = -1
        
            for x in range(width):
                reverseX: int = -(x+1)
                
                if forest[y][x] > highest:
                    highest           = forest[y][x]
                    visibleMask[y][x] = True
                    
                if forest[y][reverseX] > reverseHighest:
                    reverseHighest           = forest[y][reverseX]
                    visibleMask[y][reverseX] = True
                    
        # Testing columns
        for x in range(width):
            highest:        int = -1
            reverseHighest: int = -1
            
            for y in range(height):
                reverseY: int = -(y+1)
                
                if forest[y][x] > highest:
                    highest           = forest[y][x]
                    visibleMask[y][x] = True
                
                if forest[reverseY][x] > reverseHighest:
                    reverseHighest           = forest[reverseY][x]
                    visibleMask[reverseY][x] = True
                    
        return sum([sum(line) for line in visibleMask])
    
if __name__ == "__main__":
    print(day8_part1_main())
