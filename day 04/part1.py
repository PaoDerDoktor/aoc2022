def day4_part1_main() -> int:
    with open("day 04/inputs.txt", 'r') as inFile:
        inLines: list[tuple[str, str]] = [(line.strip().split(",")[0], line.strip().split(",")[1]) for line in inFile.readlines()]
        
        assignments: list[tuple[tuple[int, int], tuple[int, int]]] = [
            ((int(line[0].split('-')[0]), int(line[0].split('-')[1])), (int(line[1].split('-')[0]), int(line[1].split('-')[1]))) for line in inLines
        ]
        
        covered: int = 0
        for assignment in assignments:
            if (assignment[0][0] <= assignment[1][0]) and (assignment[0][1] >= assignment[1][1]):
                covered += 1
            elif (assignment[1][0] <= assignment[0][0]) and (assignment[1][1] >= assignment[0][1]):
                covered += 1
            
        return covered

if __name__ == "__main__":
    print(day4_part1_main())
