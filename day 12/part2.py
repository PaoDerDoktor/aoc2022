from tracemalloc import start


def get_valid_neighbours(grid: list[list[str]], center: tuple[int, int]) -> set[tuple[int, int]]:
    neighbours: set[tuple[int, int]] = {(center[0]+offset[0], center[1]+offset[1]) for offset in {(1, 0), (0, 1), (-1, 0), (0, -1)}}
    
    validNeighbours: set[tuple[int, int]] = set()
    for neighbour in neighbours:
        if (not (0 <= neighbour[0] < len(grid[0]))) or (not (0 <= neighbour[1] < len(grid))):
            continue
        
        if (ord(grid[neighbour[1]][neighbour[0]]) - ord(grid[center[1]][center[0]])) >= -1:
            validNeighbours.add(neighbour)
    
    return validNeighbours

def day12_part2_main() -> int:
    with open("day 12/inputs.txt", 'r') as inFile:
        grid: list[list[str]] = [[c for c in line.strip()] for line in inFile.readlines()]
        
        height: int = len(grid)
        width:  int = len(grid[0])
        
        starts: set[tuple[int, int]] = set()
        goal:   tuple[int, int]      = (-2, -2)
        
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 'S':
                    starts.add((x, y))
                    grid[y][x] = 'a'
                elif grid[y][x] == 'a':
                    starts.add((x, y))
                elif grid[y][x] == 'E':
                    goal = (x, y)
                    grid[y][x] = 'z'
                    
        predecessor: dict[tuple[int, int], tuple[int, int]] = {goal: goal}
        dist:        dict[tuple[int, int], int]             = {goal: 0}
        queue:       list[tuple[int, int]]                  = [goal]
        
        while len(queue) != 0:
            current: tuple[int, int] = queue.pop()
            
            for neighbour in get_valid_neighbours(grid, current):
                if neighbour not in dist or dist[current]+1 < dist[neighbour]:
                    queue.append(neighbour)
                    dist[neighbour] = dist[current] + 1
                    predecessor[neighbour] = current

        bestsStarts: list[int] = sorted([dist[start] for start in starts if start in dist])
        
        return bestsStarts[0]

if __name__ == "__main__":
    print(day12_part2_main())
