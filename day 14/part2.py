from sys import maxsize

def render(rocks: dict[int, dict[int, str]], sandOrigin: tuple[int, int]) -> str:
    minX = min(rocks)
    maxX = max(rocks)
    
    minY = maxsize
    maxY = -1
    
    for k in rocks:
        if min(rocks[k]) < minY:
            minY = min(rocks[k])
        if max(rocks[k]) > maxY:
            maxY = max(rocks[k])
    
    lines: list[str] = ["" for _ in range(maxY-minY+1)]
    for c, x in enumerate(range(minX, maxX+1)):
        for l, y in enumerate(range(minY, maxY+1)):
            lines[l] += rocks.get(x, {}).get(y, '.')
    
    return '\n'.join(lines)

def intersectors(rocks: dict[int, dict[int, str]], position: tuple[int, int]) -> list[int]:
    return [height for height in rocks.get(position[0], {}) if height > position[1] and rocks[position[0]][height] != '.']

def count_sand(rocks: dict[int, dict[int, str]]) -> int:
    amount: int = 0
    for x in rocks:
        for y in rocks[x]:
            if rocks[x][y] == 'o':
                amount += 1
    return amount

def get_low_border(rocks: dict[int, dict[int, str]]) -> int:
    maxY: int = -1
    for x in rocks:
        for y in rocks[x]:
            if y > maxY:
                maxY = y
    return maxY+2

def day14_part2_main(verbose: bool=False) -> int:
    with open("day 14/inputs.txt", 'r') as inFile:
        pathes: list[list[tuple[int, int]]] = [[(int(coord.split(',')[0]), int(coord.split(',')[1])) for coord in line.strip().split(' -> ')] for line in inFile.readlines()]
        sandOrigin: tuple[int, int]           = (500, 0)
        rocks:      dict[int, dict[int, str]] = {}
        
        for path in pathes:
            for i in range(1, len(path)):
                for x in range(min(path[i-1][0], path[i][0]), max(path[i-1][0], path[i][0])+1):
                    for y in range(min(path[i-1][1], path[i][1]), max(path[i-1][1], path[i][1])+1):
                        if x not in rocks:
                            rocks[x] = {}
                        rocks[x][y] = '#'
        
        amount: int = 0
        sourceQueue: list[tuple[int, int]] = [sandOrigin]
        sandPosition: tuple[int, int] = sandOrigin
        started: bool = False
        maxY: int = get_low_border(rocks)
        

        while len(sourceQueue) != 0:
            if verbose: print("///////////////////////////////////////////////////////////////////////"+"\n"+render(rocks, sourceQueue[-1]))
            
            if sourceQueue[-1] == sandOrigin:
                if not started:
                    started = True
                else:
                    break
            
            if rocks.get(sourceQueue[-1][0], {}).get(sourceQueue[-1][1], '.') == 'o':
                sourceQueue.pop()
                continue
            
            if (rocks.get(sourceQueue[-1][0], {}).get(sourceQueue[-1][1]+1, '.') == '.') and (sourceQueue[-1][1]+1 < maxY): # Source can go directly lower
                sourceQueue.append((sourceQueue[-1][0], sourceQueue[-1][1]+1))
            elif (rocks.get(sourceQueue[-1][0]-1, {}).get(sourceQueue[-1][1]+1, '.') == '.') and (sourceQueue[-1][1]+1 < maxY): # Source can go diag-left
                sourceQueue.append((sourceQueue[-1][0]-1, sourceQueue[-1][1]+1))
            elif (rocks.get(sourceQueue[-1][0]+1, {}).get(sourceQueue[-1][1]+1, '.') == '.') and (sourceQueue[-1][1]+1 < maxY): # Source can go diag-right
                sourceQueue.append((sourceQueue[-1][0]+1, sourceQueue[-1][1]+1))
            else: # Source is stuck
                if sourceQueue[-1][0] not in rocks:
                    rocks[sourceQueue[-1][0]] = {}
                rocks[sourceQueue[-1][0]][sourceQueue[-1][1]] = 'o'
                
        return count_sand(rocks) + 2*(maxY-1) + 1 # Taking in account the missing right pyramid slope, and it's "peak"
        
        

if __name__ == "__main__":
    print(day14_part2_main())
