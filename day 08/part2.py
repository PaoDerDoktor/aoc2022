def day8_part2_main() -> int:
    with open("day 08/inputs.txt", 'r') as inFile:
        forest: list[list[int]] = [[int(tree) for tree in line.strip()] for line in inFile.readlines()] # Adressed (height, width)
        
        height: int = len(forest)
        width:  int = len(forest[0])
        
        scenicMask: list[list[int]] = [[-1 for x in range(width)] for y in range(height)]
        
        for x in range(width):
            for y in range(height):
                
                scenicMask[y][x] = 0
                
                rightComponent: int = 0
                offset: int = 1
                # Testing on the right
                while x+offset < width:
                    rightComponent += 1

                    if forest[y][x+offset] >= forest[y][x]:
                        break
                    offset += 1
                
                leftComponent: int = 0
                offset = 1
                # Testing on the left
                while x-offset >= 0:
                    leftComponent += 1

                    if forest[y][x-offset] >= forest[y][x]:
                        break
                    offset += 1
                    
                upComponent: int = 0
                offset = 1
                # Testing up
                while y+offset < height:
                    upComponent += 1

                    if forest[y+offset][x] >= forest[y][x]:
                        break
                    offset += 1
                    
                underComponent: int = 0
                offset = 1
                # Testing under
                while y-offset >= 0:
                    underComponent += 1

                    if forest[y-offset][x] >= forest[y][x]:
                        break
                    offset += 1
                    
                scenicMask[y][x] = rightComponent * leftComponent * upComponent * underComponent
                
                    
        return max([max(line) for line in scenicMask])
    
if __name__ == "__main__":
    print(day8_part2_main())
