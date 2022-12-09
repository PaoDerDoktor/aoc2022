def day9_part2_main() -> int:
    with open("day 09/inputs.txt", 'r') as inFile:
        headMoves: list[tuple[str, int]] = [(line[0], int(line.strip()[1:])) for line in inFile.readlines()]
        knotsPos: list[tuple[int, int]] = [(0, 0) for _ in range(10)]
        
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
                knotsPos[0] = (knotsPos[0][0]+offset[0], knotsPos[0][1]+offset[1])
                
                for i in range(1, len(knotsPos)):
                    if knotsPos[i] == knotsPos[i-1]:
                        continue
                    
                    nearTail: set[tuple[int, int]] = {(knotsPos[i  ][0]+k, knotsPos[i  ][1]+l) for k in (-1, 0, 1) for l in (-1, 0, 1)} - {knotsPos[i]}
                    nearHead: set[tuple[int, int]] = {(knotsPos[i-1][0]+k, knotsPos[i-1][1]+l) for k in (-1, 0, 1) for l in (-1, 0, 1)} - {knotsPos[i-1]}
                    
                    if knotsPos[i-1] in nearTail:
                        continue
                    
                    commons: set[tuple[int, int]] = nearTail.intersection(nearHead)
                    
                    if len(commons) <= 3:
                        minDist: int = 99
                        bestPos: tuple[int, int] = list(commons)[0]
                        
                        for common in commons:
                            comDist: int = abs(knotsPos[i-1][0]-common[0]) + abs(knotsPos[i-1][1]-common[1])
                            if minDist > comDist:
                                minDist = comDist
                                bestPos = common
                        
                        knotsPos[i] = bestPos
                        continue
                
                tailVisited.add(knotsPos[-1])
                
        return len(tailVisited) 

if __name__ == "__main__":
    print(day9_part2_main())
