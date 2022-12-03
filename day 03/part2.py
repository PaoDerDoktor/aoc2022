ALPHABET:  str            = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHADICT: dict[str, int] = {l: i for i, l in enumerate(ALPHABET)}

def day3_part2_main() -> int:
    with open("day 03/inputs.txt", 'r') as inFile:
        inLines: list[str] = [inLine.strip() for inLine in inFile.readlines()]
        
        groups: list[tuple[str, str, str]] = [(inLines[i], inLines[i+1], inLines[i+2]) for i in range(0, len(inLines), 3)]
        
        badgesPriorities: list[int] = []
        for group in groups:
            for item in group[0]:
                if item in group[1] and item in group[2]:
                    badgesPriorities.append(ALPHADICT[item])
                    break
                
        return sum(badgesPriorities)
    
if __name__ == "__main__":
    print(day3_part2_main())
