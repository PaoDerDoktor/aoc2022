def day6_part1_main() -> int:
    with open("day 06/inputs.txt", 'r') as inFile:
        data: str = inFile.read().strip()
        
        for i in range(3, len(data)-1):
            elementsSet: set[str] = {l for l in data[i-3:i+1]}
            if len(elementsSet) == 4:
                return i+1
        
        return -1
    
if __name__ == "__main__":
    print(day6_part1_main())
