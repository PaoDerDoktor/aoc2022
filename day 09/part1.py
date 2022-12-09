def day9_part1_main() -> int:
    with open("day 09/inputs.txt", 'r') as inFile:
        headMoves: list[tuple[str, int]] = [(line[0], int(line.strip()[1:])) for line in inFile.readlines()]
        headPos: tuple[int, int] = (0, 0)
        tailPos: tuple[int, int] = (0, 0)
        
        tailVisited: set[tuple[int, int]] = {(0,0)}
        
        for move in headMoves:
            offset: tuple[int, int] = (-99, -99)
            
            if move[0] == "L":
                offset = (-1, 0)
            elif move[0] == "R":
                offset = (1, 0)
            elif move[0] == "D":
                offset = (0, -1)
            elif move[0] == "U":
                offset = (0, 1)
            else:
                raise NotImplementedError(f"Direction `{move[0]}` is not implemented.")
            
            for _ in range(move[1]):
                headPos = (headPos[0]+offset[0], headPos[1]+offset[1])
                
                tailDist: tuple[int, int] = (headPos[0]-tailPos[0], headPos[1]-tailPos[1])
                
                if abs(tailDist[0])+abs(tailDist[1]) == 2:
                    if abs(tailDist[0]) >= 2:
                        tailPos = (tailPos[0]+1 if tailDist[0] > 0 else tailPos[0]-1, tailPos[1])
                    elif abs(tailDist[1]) >= 2:
                        tailPos = (tailPos[0], tailPos[1]+1 if tailDist[1] > 0 else tailPos[1]-1)
                elif abs(tailDist[0])+abs(tailDist[1]) == 3:
                    if abs(tailDist[0]) == 1:
                        tailPos = (tailPos[0]+1 if tailDist[0] > 0 else tailPos[0]-1, tailPos[1])
                    elif abs(tailDist[1]) == 1:
                        tailPos = (tailPos[0], tailPos[1]+1 if tailDist[1] > 0 else tailPos[1]-1)
                        
                    if abs(tailDist[0]) == 2:
                        tailPos = (tailPos[0]+1 if tailDist[0] > 0 else tailPos[0]-1, tailPos[1])
                    elif abs(tailDist[1]) == 2:
                        tailPos = (tailPos[0], tailPos[1]+1 if tailDist[1] > 0 else tailPos[1]-1)
                
                tailVisited.add(tailPos)
                
        return len(tailVisited) 

if __name__ == "__main__":
    print(day9_part1_main())
