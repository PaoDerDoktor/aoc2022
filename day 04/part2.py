def day4_part2_main() -> int:
    with open("day 04/inputs.txt", 'r') as inFile:
        inLines: list[tuple[str, str]] = [(line.strip().split(",")[0], line.strip().split(",")[1]) for line in inFile.readlines()]
        
        assignments: list[tuple[tuple[int, int], tuple[int, int]]] = [
            ((int(line[0].split('-')[0]), int(line[0].split('-')[1])), (int(line[1].split('-')[0]), int(line[1].split('-')[1]))) for line in inLines
        ]
        
        covered: int = 0
        for assignment in assignments:
            firstRange  = range(assignment[0][0], assignment[0][1]+1)
            for area in firstRange:
                if assignment[1][0] <= area <= assignment[1][1]:
                    covered += 1
                    break
            
        return covered

if __name__ == "__main__":
    print(day4_part2_main())
