ALPHABET:  str            = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHADICT: dict[str, int] = {l: i for i, l in enumerate(ALPHABET)}

def day3_part1_main() -> int:
    with open("day 03/inputs.txt", 'r') as inFile:
        rucksacks: list[tuple[str, str]] = [(rucksack.strip()[:int(len(rucksack.strip())/2)], rucksack.strip()[int(len(rucksack.strip())/2):]) for rucksack in inFile.readlines()]
        
        priorities: int = 0
        
        for rucksack in rucksacks:
            for item in rucksack[0]:
                if item in rucksack[1]:
                    priorities += ALPHADICT[item]
                    break
        
        return priorities
    
if __name__ == "__main__":
    print(day3_part1_main())
